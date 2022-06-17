## Getgit

**Getgit** - terminal utility that allows to clone user repositories.

`It allows to clone only public repositories because of using web parsing.`


## How to install

### First way

1. Install Python3.
2. Install Getgit with the following `pip` command from the command prompt:

```sh
pip install getgit
```

### Second way

1. Install Python3.
2. Clone Getgit with git command:
3. Go to the directory `getgit`:
4. Use Python command for installing scripts below:

```sh
git clone https://github.com/Krai53n/getgit.git
cd getgit
python setup.py install_scripts
```


## How to use it

Run cli:
```
getgit
```

Clone repository of user that setted configuration file
```
getgit -r rep_name
```

Change settings in configuration file:
```
getgit -s service_name -n nick_name
```

Clone repository of some user:
```
getgit -s service_name -n nick_name -r rep_name
```
