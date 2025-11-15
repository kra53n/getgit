package main

import (
	"context"
	"fmt"
	"log/slog"
	"os"
	"os/exec"
	"runtime"
	"strconv"
	"strings"
)

func main() {
	var err error
	var c *exec.Cmd
	var build []string
	var progName = "gg"
	var buildDir = "build"
	var progPath = buildDir + "/" + progName
	if runtime.GOOS == "windows" {
		progPath += ".exe"
	}
	var srcs = []string{"main.go"}
	var args = os.Args

	args = os.Args[1:]

	// clean
	if len(args) > 0 && (args[0] == "clean" || args[0] == "c") {
		// TODO(kra53n) consider flags package
		logger.Info("delete " + "./" + buildDir)
		os.RemoveAll(buildDir)
		return
	}
	// logger.Error("does not know " + args[0] + " command")

	// format
	build = append(build, "go")
	build = append(build, "fmt")

	for _, src := range srcs {
		build = append(build, src)
	}

	c = execCommand(build...)
	c.Stderr = os.Stdout
	c.Run()

	// build
	build = build[:0]

	if _, err := os.Stat(progPath); os.IsNotExist(err) {
		logger.Info("create ./build directory")
		os.Mkdir(buildDir, 0777)
	}

	build = append(build, "go")
	build = append(build, "build")

	build = append(build, "-o")
	build = append(build, progPath)

	for _, src := range srcs {
		build = append(build, src)
	}

	c = execCommand(build...)
	c.Stderr = os.Stdout
	if err = c.Run(); err != nil {
		return
	}

	// run
	if len(args) > 0 && (args[0] == "run" || args[0] == "r") {
		args := args[1:]
		build = build[:0]

		build = append(build, "./" + progPath)

		// build = append(build, "-help")

		// build = append(build, "-rep")
		// build = append(build, "hello")

		// build = append(build, "repo")

		build = append(build, args...)

		c = execCommand(build...)
		c.Stderr = os.Stdout
		c.Stdout = os.Stdout
		c.Run()
		return
	}
}

// ----------------------------------------------------------------------------
// --- build.go system implementation
//
// 1. Run `go build build.go` to startup building system.
// 2. Run `./build` to use building system.

// Globals
var (
	srcFilename string
	binFilename string
	src         os.FileInfo
	logger      *slog.Logger = slog.New(LoggerHandler{})

	// build.src modification time that will saved to binary to have an
	// opportunity to rebuild urself
	modtime string
)

type LoggerHandler struct{}

func (l LoggerHandler) Enabled(context.Context, slog.Level) bool { return true }

// Build the `[r.Level.String()] r.Message[({attr1, attr2})]` string
// and than print it. For example we can print this strings:
// - [ERROR] Some error occured
// - [WARN] Some error occured (sword=art, art=online)
//
// * We can use variable with Writable interface to not only print in
// stdout but in other places like stderr or write logs to files.
func (l LoggerHandler) Handle(c context.Context, r slog.Record) error {
	var b strings.Builder

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
	fmt.Println(b.String())

	return nil
}

func (l LoggerHandler) WithAttrs(attrs []slog.Attr) slog.Handler { return nil }
func (l LoggerHandler) WithGroup(name string) slog.Handler       { return nil }

func execCommand(s ...string) *exec.Cmd {
	logger.Info(strings.Join(s, " "))
	return exec.Command(s[0], s[1:]...)
}

func init() {
	var err error

	srcFilename = "build.go"
	binFilename = "b"
	if runtime.GOOS == "windows" {
		binFilename += ".exe"
	}

	if src, err = os.Stat(srcFilename); err != nil {
		logger.Error(err.Error())
		os.Exit(1)
	}

	if needToRebuild() {
		rebuildUrself()
	}
}

func needToRebuild() bool {
	if modtime == "" {
		return true
	}
	if modtime != strconv.FormatInt(src.ModTime().Unix(), 10) {
		return true
	}
	return false
}

func rebuildUrself() {
	var err error
	var cmd *exec.Cmd

	logger.Info("rebuild urself")

	modtime := strconv.FormatInt(src.ModTime().Unix(), 10)
	cmd = execCommand("go", "build", "-ldflags", "-X main.modtime="+modtime, "-o", binFilename, srcFilename)
	cmd.Stderr = os.Stdout
	if err = cmd.Run(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	var c []string
	c = append(c, "./" + binFilename)
	c = append(c, os.Args[1:]...)

	cmd = execCommand(c...)
	cmd.Stderr = os.Stdout
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	err = cmd.Start()
	if err != nil {
		logger.Error(fmt.Sprintf("starting process: %v", err))
		return
	}
	err = cmd.Wait()
	if err != nil {
		logger.Error("child process finished: %v\n", err)
	}

	os.Exit(0)
}
