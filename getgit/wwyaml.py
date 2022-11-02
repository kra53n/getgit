"""wwyaml - work with yaml"""

from yaml import load, FullLoader, dump
from dataclasses import dataclass
from pathlib import Path
from os import makedirs
import os.path
from sys import exit

from .config import USER_CONFIG_DIR


@dataclass
class UserData:
    service: str = ''
    nickname: str = ''
    port: str = 'https'  # or ssh


def load_dict_to_UserData(dct: dict, data: UserData) -> UserData:
    for key in data.__dict__.keys():
        if key in dct:
            data.__dict__[key] = dct[key]
    return data


def change_UserData(data1: UserData, data2: UserData) -> UserData:
    for key, val in data2.__dict__.items():
        if val:
            data1.__dict__[key] = val
    return data1


def create_file(path: Path = USER_CONFIG_DIR, filename: str = 'config.yaml'):
    """Create file in define path"""
    if not os.path.isdir(path):
        makedirs(path)
    with open(path / filename, "w") as f:
        fields = (f'{field}:' for field in UserData.__dict__.keys())
        f.write('\n'.join(fields))


def load_data(path: Path = USER_CONFIG_DIR, filename: str = 'config.yaml') -> UserData | None:
    """Return data from config.yaml"""
    try:
        with open(path / filename) as f:
            return load_dict_to_UserData(load(f, Loader=FullLoader), UserData())
    except FileNotFoundError:
        create_file()
        return


def put_data(data: UserData, path: Path = USER_CONFIG_DIR, filename: str = 'config.yaml'):
    """Put service(github, gitlab, ...) and nickname in config.yaml"""
    with open(path / filename, "w") as f:
        dump(data.__dict__, f)


def check_filling_of_data(path: Path = USER_CONFIG_DIR, filename: str = 'config.yaml'):
    """
    Return 1 if service and nickname in config.yaml exist.  
    Otherwise return 0.
    """
    data = load_data(path)
    try:
        fields = ('service', 'nickname')
        return all(map(lambda x: x in data.__dict__.keys(), fields)) and None not in (data.__dict__[field] for field in fields)
    except TypeError:
        print(f"Config file was add in {USER_CONFIG_DIR / filename}")
        exit()
