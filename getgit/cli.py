from sys import argv, exit, platform

if platform == 'linux':
    from simple_term_menu import TerminalMenu

from .clone import clone_rep
from .constants import CONFIG_DIR
from .parse import get_config_data, parse_reps, get_url
from .wwyaml import check_filling_of_data, load_data, put_data


def introduce_program():
    print('''
    Welcome to getgit! I hope this script will useful for you!
    From people to people (^_−)☆.
    '''
    )


def print_wishes():
    print(f"\nEverything is ready! If you want change something "
          f"just go to {CONFIG_DIR} and change there data")


def dl_rep(rep_name):
    data_config = load_data()
    clone_rep(data_config['service'], data_config['nickname'], rep_name)
    exit()


def dl_all():
    """
    Download all visible repositories of user
    """
    data_config = load_data()
    reps_names = parse_reps(data_config['service'], get_url(data_config['service'], data_config['nickname']))
    for rep_name in reps_names:
        clone_rep(data_config['service'], data_config['nickname'], rep_name)
    exit()


class Os:
    def __init__(self):
        self.data = check_filling_of_data()


class GnuLinux(Os):
    def __init__(self):
        super().__init__()

        if self.data:
            """If user have the data in $HOME/.config/config.yaml"""
            menu_title = "Choose repository to clone\n"
            data_config = load_data()
            menu_items = parse_reps(data_config['service'], get_url(data_config['service'], data_config['nickname']))
        else:
            """If user start this program for the first time"""
            introduce_program()
            menu_title = 'Choose git version: '
            menu_items = get_config_data().keys()

        terminal_menu = TerminalMenu(menu_entries=menu_items, title=menu_title)
        menu_entry_index = terminal_menu.show()

        if self.data:
            if menu_entry_index is not None:
                rep_name = menu_items[menu_entry_index]
                dl_rep(rep_name)
        else:
            git_service = get_config_data().keys()[menu_entry_index]
            nickname = input("Write you nickname: ")
            put_data(git_service, nickname)
            print_wishes()


class Windows(Os):
    def __init__(self):
        super().__init__()

        if self.data:
            """If user have the data in .config/config.yaml"""
            print("\tChoose repository to clone\n")
            data_config = load_data()
            rep_name = self._select_option(
                'Choose repository: ',
                parse_reps(data_config['service'], get_url(data_config['service'], data_config['nickname'])),
            )
            clone_rep(data_config['service'], data_config['nickname'], rep_name)
        else:
            """If user start this program for the first time"""
            introduce_program()
            git_service = self._select_option('Choose git version: ', get_config_data().keys())
            nickname = input("Write your nickname: ")
            put_data(git_service, nickname)
            print_wishes()

    def _select_option(self, title: str, opts: list) -> int:
        for idx, opt in enumerate(opts, 1):
            print(f'\t{idx}. {opt}')
        print()
        while not (idx := input(title)).isdigit() or not 1 <= int(idx) <= len(opts):
            print(f'Put digit from {1} to {len(opt)}')
        return opts[int(idx)-1]


def cli():
    if platform == 'win32':
        Windows()
    if platform == 'linux':
        GnuLinux()
