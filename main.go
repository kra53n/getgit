// TODO(kra53n): add error while does not provided repositories in arguments

package main

import (
	"context"
	"flag"
	"fmt"
	"log/slog"
	"os"
	"os/exec"
	"strings"
)

type Setup struct {
	nickname     string   // nickname (kra53n, rsc, ...)
	repositories []string // list of repositories (getgit, ...)
	service      string   // git-hosting (github, gitlab, ...)
	protocol     string   // protocol (ssh, https, ...)
	directory    string   // destination directory (C:\Users\SomeUser\Desktop\Repositories\RepositoryName on Windows or ~/Desktop/repositories/repository_name on Linux)
}

type Config map[string]Setup

var config = Config{
	"github": Setup{
		service:  "github.com",
		nickname: "kra53n",
		protocol: "ssh",
	},
	"gitlab": Setup{
		service:  "gitlab.com",
		nickname: "kra53n",
		protocol: "ssh",
	},
}

var setup Setup
var useByDefault string = "github"

func init() {
	// get arguments
	nickname := flag.String("name", "", "nickname on git-hosting")
	repository := flag.String("rep", "", "repository on git-hosting")
	service := flag.String("service", "", "service like github or gitlab")
	protocol := flag.String("protocol", "", "protocol to download the repository from git-hosting, like https or ssh")
	directory := flag.String("dir", "", "destination directory for repository, e.g.: ~/Desktop/repositories/getigt")
	use := flag.String("use", "", "select setup from config")
	list := flag.Bool("list", false, "print setup list")
	print := flag.Bool("print", false, "print whole config")

	// parse arguments
	oldUsage := flag.Usage
	flag.Usage = func() {
		oldUsage()
	}
	flag.Parse()

	// process argument values
	if *list {
		fmt.Println(config.formatNames())
		os.Exit(0)
	}

	if *print {
		fmt.Println(config.String())
		os.Exit(0)
	}

	if *use == "" {
		*use = useByDefault
	}
	setup.use(*use)

	if *nickname != "" {
		setup.nickname = *nickname
	}
	if *repository != "" {
		setup.repositories = append(setup.repositories, *repository)
	}
	if *service != "" {
		setup.service = *service
	}
	if *protocol != "" {
		setup.protocol = *protocol
	}
	if *directory != "" {
		setup.directory = *directory
	}

	for _, repository := range flag.Args() {
		setup.repositories = append(setup.repositories, repository)
	}

	logger.Debug("func init()")
	logger.Debug(fmt.Sprintf("NArg: %d", flag.NArg()))
	logger.Debug(fmt.Sprintf("NFlag: %d", flag.NFlag()))
	logger.Debug(fmt.Sprintf("nickname: %s", *nickname))
	logger.Debug(fmt.Sprintf("repository: %s", *repository))
	logger.Debug(fmt.Sprintf("service: %s", *service))
	logger.Debug(fmt.Sprintf("protocol: %s", *protocol))
	logger.Debug(fmt.Sprintf("directory: %s", *directory))
	logger.Debug(fmt.Sprintf("use: %s", *use))
	logger.Debug(fmt.Sprintf("print: %t", *print))
	logger.Debug(fmt.Sprintf("list: %t", *list))
	logger.Debug(fmt.Sprintf("flag.Args: %v", flag.Args()))
	logger.Debug("")

	if len(setup.repositories) == 0 {
		flag.Usage()
		os.Exit(1)
	}
}

func main() {
	var arr []string

	logger.Debug("func main()")

	for _, repository := range setup.repositories {
		arr = arr[:0]
		arr = append(arr, "git")
		arr = append(arr, "clone")
		arr = append(arr, uri(repository))

		if setup.directory != "" {
			arr = append(arr, setup.directory+"/"+repository)
		}

		logger.Debug(strings.Join(arr, " "))

		cmd := exec.Command(arr[0], arr[1:]...)
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		cmd.Run()
	}
}

var logger *slog.Logger = slog.New(LoggerHandler{})

var debugFile *os.File = os.Stderr // debug file descriptor for debug logger mode

func (s *Setup) String() string {
	var b strings.Builder

	const margin string = "    "
	const separator string = "\r\n"

	writeFramed := func(k, v string) {
		b.WriteString(margin)
		b.WriteString(k)
		b.WriteString(": ")
		b.WriteString(v)
		b.WriteString(separator)
	}

	writeFramed("nickname", s.nickname)
	writeFramed("service", s.service)
	writeFramed("protocol", s.protocol)
	writeFramed("directory", s.directory)

	return strings.TrimRight(b.String(), separator)
}

func (c *Config) formatNames() string {
	var b strings.Builder
	const margin string = ""
	const separator string = "\r\n"
	for name, _ := range *c {
		b.WriteString(margin)
		b.WriteString(name)
		b.WriteString(separator)
	}
	s := b.String()
	return s[:len(s)-len(separator)]
}

func (c *Config) String() string {
	var b strings.Builder
	const margin string = ""
	const separator string = "\r\n"
	for name, setup := range *c {
		b.WriteString(margin)
		b.WriteString(name)
		b.WriteString(separator)
		b.WriteString(setup.String())
		b.WriteString(separator)
		b.WriteString(separator)
	}
	return strings.TrimRight(b.String(), separator)
}

func (s *Setup) use(name string) {
	v, ok := config[name]
	if !ok {
		fmt.Println(fmt.Sprintf("no setup %s in config, use `-list` flag to see setups", name))
		os.Exit(1)
	}
	if s.nickname == "" && v.nickname != "" {
		s.nickname = v.nickname
	}
	if s.service == "" && v.service != "" {
		s.service = v.service
	}
	if s.protocol == "" && v.protocol != "" {
		s.protocol = v.protocol
	}
	if s.directory == "" && v.directory != "" {
		s.directory = v.directory
	}
}

func uri(repository string) string {
	switch setup.protocol {
	case "https":
		return fmt.Sprintf("https://%s/%s/%s.git", setup.service, setup.nickname, repository)
	case "ssh":
		return fmt.Sprintf("git@%s:%s/%s.git", setup.service, setup.nickname, repository)
	}
	logger.Debug("func uri()")
	logger.Debug("protocol does not supported")
	logger.Debug("")
	return ""
}

type LoggerHandler struct{}

func (l LoggerHandler) Enabled(context.Context, slog.Level) bool { return true }
func (l LoggerHandler) WithAttrs(attrs []slog.Attr) slog.Handler { return nil }
func (l LoggerHandler) WithGroup(name string) slog.Handler       { return nil }

func (l LoggerHandler) Handle(c context.Context, r slog.Record) error {
	var file *os.File
	var b strings.Builder

	switch r.Level {
	case slog.LevelDebug:
		file = debugFile
	default:
		file = os.Stdout
	}

	b.WriteByte('[')
	b.WriteString(r.Level.String())
	b.WriteByte(']')

	b.WriteByte(' ')

	b.WriteString(r.Message)

	numAttrs := r.NumAttrs()
	if numAttrs > 0 {
		b.WriteByte(' ')
		b.WriteByte('(')
		attrIdx := 0
		r.Attrs(func(a slog.Attr) bool {
			attrIdx++
			b.WriteString(a.String())
			if attrIdx != numAttrs {
				b.WriteByte(',')
				b.WriteByte(' ')
			}
			return true
		})
		b.WriteByte(')')
	}
	b.WriteByte('\r')
	b.WriteByte('\n')
	fmt.Fprintf(file, b.String())

	return nil
}
