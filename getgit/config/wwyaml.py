"""wwyaml - work with yaml"""

from yaml import load
from yaml import FullLoader
from yaml import dump

from sys import exit
from sys import platform
from os import mkdir


from pathlib import Path
path_conf_file = str(Path.home())
if platform == "linux":
    path_conf_file += "/.config/getgit/config.yaml"
if platform == "win32":
    # TODO: need here r or not
    path_conf_file += r"\.config\getgit\config.yaml"


def create_file(path=path_conf_file):
    """Create file in define path
    """
    # TODO: check working of mkdir
    # make simulation with path and actions that located under
    mkdir(path[:-12])
    with open(path, "w") as f:
        f.write("service:\nnickname:")

def load_data(path=path_conf_file):
    """Return parsed data from config.yaml
    """
    try:
        with open(path) as f:
            data = load(f, Loader=FullLoader)
        return data

    except FileNotFoundError:
        create_file()

def put_data(service, nickname, path=path_conf_file):
    """Put service(github, gitlab, ...) and nickname inot config.yaml
    """
    data = {"service": service, "nickname": nickname}
    with open(path, "w") as f:
        dump(data, f)

def check_filling_of_data(path=path_conf_file):
    """If service and nickname in config.yaml exist then return 1.
    Otherwise return 0
    """
    data = load_data(path)
    try:
        if (data["service"] == None) and (data["nickname"] == None):
            return 0
        return 1
    except TypeError:
        print("Config file was add in ~/.config/getgit/ as config.yaml")
        exit()
