"""Cli interface for getgit"""

from sys import argv, exit

from wwyaml import check_filling_of_data, load_data, put_data
from clone import clone_notabug_rep, clone_github_rep
from parse import parse_reps, get_url
from constants import CONFIG_DIR


def introduce_program():
    txt = """
    Welcome to getgit! I hope this script will useful for you!
    From people to people (^_−)☆.
    """
    print(txt)


def dl_rep(rep_name):
    """
    Download repository that have `name` title of user
    """
    data_config = load_data()
    service = data_config["service"]
    args = data_config["nickname"], rep_name
    switch = {service == "github": clone_github_rep, service == "notabug": clone_notabug_rep}
    switch.get(True)(*args)
    exit()


def dl_all():
    """
    Download all visible repositories of user
    """
    data_config = load_data()
    reps_names = parse_reps(data_config['service'], 'https://github.com/kra53n?tab=repositories')
    switch = {'github': clone_github_rep, 'notabug': clone_notabug_rep}
    for rep_name in reps_names:
        switch[data_config['service']](data_config['nickname'], rep_name)
    exit()


def ask_git_version_service():
    txt = "Choose git service that you use:\n"
    gits = ("github", "gitlab", "notabug")
    return txt, gits


def wishes():
    print(f"\nEverything is ready! If you want change something "
          f"just go to {CONFIG_DIR} and change there data")


class Os:
    """
    This is parent class of other classes such as GnuLinux or Windows
    """
    def __init__(self):
        self.data = check_filling_of_data()


class GnuLinux(Os):
    """
    Cli interface for GnuLinux systems
    """
    def __init__(self):
        from simple_term_menu import TerminalMenu
        super().__init__()

        if self.data == 0:
            """If user start this program for the first time"""
            introduce_program()
            menu_title = ask_git_version_service()[0]
            menu_items = ask_git_version_service()[1]
        if self.data == 1:
            """If user have the data in $HOME/.config/config.yaml"""
            menu_title = "Choose repository to clone\n"
            data_config = load_data()
            menu_items = parse_reps(data_config['service'], get_url(data_config['service'], data_config['nickname']))

        terminal_menu = TerminalMenu(menu_entries=menu_items, title=menu_title)
        menu_entry_index = terminal_menu.show()

        if self.data == 0:
            git_service = ask_git_version_service()[1][menu_entry_index]
            nickname = input("Write you nickname: ")
            put_data(git_service, nickname)
            wishes()
        if self.data == 1:
            if menu_entry_index is not None:
                # if user decided to quit from program
                rep_name = menu_items[menu_entry_index]
                dl_rep(rep_name)


class Windows(Os):
    """Child of Os class
    Cli interface for Windows or OS that
    not support `simple_term_menu`
    """
    def __init__(self):
        super().__init__()
        if self.data == 0:
            """If user start this program for the first time"""
            introduce_program()
            git_service = self.choose_git_version_service_cli()
            nickname = input("Write your nickname: ")

            put_data(git_service, nickname)
            wishes()

        if self.data == 1:
            """If user have the data in .config\config.yaml"""
            print("\tChoose repository to clone\n")
            data_config = load_data()
            rep_name = self.choose_reps_cli(
                parse_reps(data_config['service'], get_url(data_config['service'], data_config['nickname']))
            )
            clone_github_rep(data_config["nickname"], rep_name)

    def choose_git_version_service_cli(self):
        services = ask_git_version_service()[1]
        for i in range(len(services)):
            print("\t{}. {}".format(i + 1, services[i]))
        service_num = int(input("\nChoose git version: ")) - 1
        return services[service_num]

    def choose_reps_cli(self, reps):
        """
        Allow user choose reps and return number of it.
        Reps have list type of data
        """
        for i in range(len(reps)):
            print("\t{}. {}".format(i + 1, reps[i]))
        reps_num = input("\nChoose rep: ")
        reps_num = int(reps_num) - 1
        return reps[reps_num]


def cli():
    from sys import platform
    if platform == "win32":
        Windows()
    if platform == "linux":
        GnuLinux()


if __name__ == "__main__":
    cli()
