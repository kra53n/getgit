from sys import argv, exit

from .clone import clone_rep
from .constants import CONFIG_DIR
from .parse import parse_reps, get_url
from .wwyaml import check_filling_of_data, load_data, put_data


def introduce_program():
    print('''
    Welcome to getgit! I hope this script will useful for you!
    From people to people (^_−)☆.
    '''
    )


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


def ask_git_version_service():
    # NOTE: delete this func and use parse.yaml
    txt = "Choose git service that you use:\n"
    gits = "github", "gitlab", "notabug"
    return txt, gits


def print_wishes():
    print(f"\nEverything is ready! If you want change something "
          f"just go to {CONFIG_DIR} and change there data")


class Os:
    def __init__(self):
        self.data = check_filling_of_data()


class GnuLinux(Os):
    def __init__(self):
        from simple_term_menu import TerminalMenu
        super().__init__()

        if self.data:
            """If user start this program for the first time"""
            introduce_program()
            menu_title = ask_git_version_service()[0]
            menu_items = ask_git_version_service()[1]
        else:
            """If user have the data in $HOME/.config/config.yaml"""
            menu_title = "Choose repository to clone\n"
            data_config = load_data()
            menu_items = parse_reps(data_config['service'], get_url(data_config['service'], data_config['nickname']))

        terminal_menu = TerminalMenu(menu_entries=menu_items, title=menu_title)
        menu_entry_index = terminal_menu.show()

        if self.data:
            git_service = ask_git_version_service()[1][menu_entry_index]
            nickname = input("Write you nickname: ")
            put_data(git_service, nickname)
            print_wishes()
        else:
            if menu_entry_index is not None:
                # if user decided to quit from program
                rep_name = menu_items[menu_entry_index]
                dl_rep(rep_name)


class Windows(Os):
    def __init__(self):
        super().__init__()
        if self.data:
            """If user start this program for the first time"""
            introduce_program()
            git_service = self._select_option('Choose git version: ', ask_git_version_service()[1])
            nickname = input("Write your nickname: ")

            put_data(git_service, nickname)
            print_wishes()
        else:
            """If user have the data in .config/config.yaml"""
            print("\tChoose repository to clone\n")
            data_config = load_data()
            rep_name = self._select_option(
                'Choose repository: ',
                parse_reps(data_config['service'], get_url(data_config['service'], data_config['nickname'])),
            )
            clone_rep(data_config['service'], data_config['nickname'], rep_name)

    def _select_option(self, title: str, opts: list) -> int:
        for idx, opt in enumerate(opts, 1):
            print(f'\t{idx}. {opt}')
        print()
        while not (idx := input(title)).isdigit() or not 1 <= int(idx) <= len(opt):
            print(f'Put digit from {1} to {len(opt)}')
        return opts[int(idx)-1]


def cli():
    from sys import platform
    if platform == "win32":
        Windows()
    if platform == "linux":
        GnuLinux()
