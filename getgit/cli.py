from sys import platform, exit
from typing import Sequence

if platform == 'linux':
    from simple_term_menu import TerminalMenu

from .clone import clone_rep
from .constants import CONFIG_DIR, CONFIG_NAME
from .parse import get_parse_config_data, parse_reps, get_url
from .wwyaml import UserData, check_filling_of_data, load_data, put_data


def introduce_program():
    space = ' ' * 4
    print(f'\n{space}Welcome to getgit! I hope this script will be useful for you!'
          f'\n{space}By people for people (^_−)☆.\n')


def print_wishes():
    print(f'\nEverything is ready! If you want to change settings '
          f'just go to config dir {CONFIG_DIR} and change there data')


def print_cfg_info():
    file = CONFIG_DIR / CONFIG_NAME
    abs_path = str(file.absolute())
    if not file.exists():
        print('Config does not exist yet in {abs_path}')
        return
    print(f'Config info in {abs_path}\n')
    print(file.read_text())


def dl_rep(rep_name: str):
    user_data = load_data()
    clone_rep(user_data, rep_name)
    exit()


def dl_all():
    """
    Download all visible repositories of user
    """
    user_data = load_data()
    reps_names = parse_reps(user_data)
    for rep_name in reps_names:
        clone_rep(user_data, rep_name)
    exit()


def get_num_from_user(title: str, error_message: str, num_range: range) -> int:
    while not (num := input(title)).isdigit() or not int(num) in num_range:
        print(error_message)
    return int(num)


class Os:
    def __init__(self):
        self.data = check_filling_of_data()


class GnuLinux(Os):
    def __init__(self):
        super().__init__()

        if self.data:
            """If user have the data in $HOME/.config/config.yaml"""
            menu_title = "Choose repository to clone\n"
            user_data = load_data()
            menu_items = parse_reps(user_data)
        else:
            """If user start this program for the first time"""
            introduce_program()
            menu_title = 'Git service: '
            menu_items = tuple(get_parse_config_data().keys())

        terminal_menu = TerminalMenu(menu_entries=menu_items, title=menu_title)
        menu_entry_index = terminal_menu.show()

        if self.data:
            if menu_entry_index is not None:
                rep_name = menu_items[menu_entry_index]
                dl_rep(rep_name)
        else:
            user_data = UserData(
                service=menu_items[menu_entry_index],
                nickname=input('Nickname: '))
            put_data(user_data)
            print_wishes()


class Windows(Os):
    def __init__(self):
        super().__init__()

        if self.data:
            """If user have the data in .config/config.yaml"""
            print("\tChoose repository to clone\n")
            user_data = load_data()
            rep_name = self._select_option(
                'Choose repository: ',
                parse_reps(user_data),
            )
            clone_rep(user_data, rep_name)
        else:
            """If user start this program for the first time"""
            introduce_program()
            user_data = UserData(
                service=self._select_option('Git service: ', tuple(get_parse_config_data().keys())),
                nickname=input('Nickname: '),
                port=input('Port (ssh or https) default - https: '))
            put_data(user_data)
            print_wishes()

    def _select_option(self, title: str, opts: Sequence) -> str:
        for idx, opt in enumerate(opts, 1):
            print(f'\t{idx}. {opt}')
        print()
        idx = get_num_from_user(title, f'Put digit from 1 to {len(opts)}', range(1, len(opts) + 1))
        return opts[idx - 1]


def cli():
    if platform == 'win32':
        Windows()
    if platform == 'linux':
        GnuLinux()
