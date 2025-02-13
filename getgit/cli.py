from sys import platform, exit
from typing import Sequence
from dataclasses import dataclass

from .clone import clone_rep
from .config import USER_CONFIG_DIR, USER_CONFIG_NAME
from .parse import get_parse_config_data, parse_reps, get_url
from .wwyaml import UserData, check_filling_of_data, load_data, put_data



MENU_TITLE_CHOOSE_REP = '\nChoose repository to clone\n'
SPACES = ' ' * 4


def print_cfg_info():
    file = USER_CONFIG_DIR / USER_CONFIG_NAME
    abs_path = str(file.absolute())
    if not file.exists():
        print('Config does not exist yet in {abs_path}')
        return
    print(f'Config info in {abs_path}\n')
    print(file.read_text())


def process_interrupts(decorator):
    def wrapper():
        try:
            decorator()
        except KeyboardInterrupt:
            exit(0)
    return wrapper


@dataclass
class Messages:
    intro = f'\n{SPACES}Welcome to getgit! I hope this script will be useful for you!' \
            f'\n{SPACES}By people for people (^_−)☆.\n'

    wishes = f'\nEverything is ready! If you want to change settings ' \
             f'just go to config dir {USER_CONFIG_DIR} and change there data'



class Os:
    def __init__(self):
        self.data = check_filling_of_data()


class Windows(Os):
    def __init__(self):
        super().__init__()

        if self.data:
            """If user have the data in .config/config.yaml"""
            print(MENU_TITLE_CHOOSE_REP)
            user_data = load_data()
            rep_name = self._select_option('Repository: ', parse_reps(user_data))
            clone_rep(user_data, rep_name)
        else:
            """If user start this program for the first time"""
            print(Messages.intro)
            user_data = UserData(
                service = self._select_option('Git service: ', tuple(get_parse_config_data().keys())),
                nickname=input('Nickname: '),
                port=input('Port (ssh or https) default - https: '))
            put_data(user_data)
            print(Messages.wishes)

    def _select_option(self, title: str, opts: Sequence) -> str:
        for idx, opt in enumerate(opts, 1):
            print(f'\t{idx}. {opt}')
        print()
        idx = get_num_from_user(title, f'Put digit from 1 to {len(opts)}', range(1, len(opts) + 1))
        return opts[idx - 1]


@process_interrupts
def cli():
    user_info = get_info_about_user_from_config()
    if user_info:
        rep_name = ask_user_rep_name()
        clone_rep(user_info, rep_name)
    else:
        print(Messages.intro)
        user_info = ask_user_for_his_info()
        save_user_info_to_config(user_info)
