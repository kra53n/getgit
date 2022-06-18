from os import system
from .parse import get_config_data


def clone_rep(service: str, nickname: str, rep_name: str, port: str = ''):
    message = get_config_data()[service]['rep'+port].replace('nickname', nickname).replace('rep_name', rep_name)
    print(message)
    system(f'git clone {message}')
