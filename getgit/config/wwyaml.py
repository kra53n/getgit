"""wwyaml - work with yaml"""

from yaml import load, FullLoader, dump
from sys import exit
from pathlib import Path
from os import makedirs


path_conf_file = str(Path.home() / ".config/getgit/config.yaml")


def create_file(path=path_conf_file):
    """Create file in define path"""
    makedirs(path[:-12])
    with open(path, "w") as f:
        f.write("service:\nnickname:")


def load_data(path=path_conf_file):
    """Return data from config.yaml"""
    try:
        with open(path) as f:
            data = load(f, Loader=FullLoader)
        return data
    except FileNotFoundError:
        create_file()


def put_data(service, nickname, path=path_conf_file):
    """Put service(github, gitlab, ...) and nickname inot config.yaml"""
    data = {"service": service, "nickname": nickname}
    with open(path, "w") as f:
        dump(data, f)


def check_filling_of_data(path=path_conf_file):
    """
    If service and nickname in config.yaml exist then return 1.
    Otherwise return 0.
    """
    data = load_data(path)
    try:
        return not all(map(lambda x: x == None, (data["service"], data["nickname"])))
    except TypeError:
        print(f"Config file was add in {path_conf_file} as config.yaml")
        exit()
