## TODO

1. [ ] explore html files of git services
   1. [ ] github
   2. [ ] botabug
   3. [ ] gitlab

- [ ] try to now what find_packages doing
- [ ] make location of config file in getgit/getgit dir
- [ ] notabug for windows
- [ ] make working with cli easy
- [ ] remove other unnecessary piece of code
- [ ] add changing of services
- [ ] load changes to pypi
- [ ] add help to cli
- [ ] add 'Usage' to README.md

### Cli commands

- change settings: `getgit (-n, --name) profile_name (-s, --service) serivce_name`
- clone rep of user `getgit (-n, --name) profile_name (-s, --service) serivce_name (-r, --rep-name) rep_name`


### Windows

- [ ] try to find interactives cli for Windows
- [ ] make exiting on Windows
- [ ] try using curses in Windows


### Solve

```sh
    mkdir(name, mode)
FileExistsError: [Errno 17] File exists: '/home/kra53n/.config/getgit'''])
```
- [ ] solve FileExistsError: [Errno 17] File exists: '/home/kra53n/.config/getgit'''])

### Ideas

- [ ] if repository already in cwd --> return message that repository already there


## COMPLETE
- [x] add notabug
- [x] add to cli -n and --name (name of repository)
- [x] add feature to download all repositories
- [x] make installing of scripts from PyPI
- [x] make documentaion
- [x] check installing of getgit
- [x] solve exception if user have not any reps on his page
- [x] solve exiting in program without any mistake
- [x] fill setup.py
- [x] make setup.py file
- [x] make exiting on Linux from program normal
- [x] make importing of requests in getgit/core/parsing.py better
- [x] check network connection
- [x] make for Winodws simple cli
- [x] test working simple-term-menu on Windows
- [x] make exceptions if name user not correct
- [x] think how structer could look like in config.yaml file
- [x] make config file in $HOME/.config/getgit/config.yaml on Linux
