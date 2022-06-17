from os import system
from .parse import get_config_data


def clone_github_rep(nickname, rep_name):
    print("git clone git@github.com:{}/{}.git".format(nickname, rep_name))
    system("git clone git@github.com:{}/{}.git".format(nickname, rep_name))


def clone_notabug_rep(nickname, rep_name):
    print("git clone https://notabug.org/{}/{}".format(nickname, rep_name))
    system("git clone https://notabug.org/{}/{}".format(nickname, rep_name))


def clone_rep(service: str, nickname: str, rep_name: str):
    message = get_config_data()[service]['rep'].replace('nickname', nickname).replace('rep_name', rep_name)
    print(message)
    system(f'git clone {message}')
