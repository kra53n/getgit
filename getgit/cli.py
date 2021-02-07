"""Cli interface for getgit"""

from config import check_filling_of_data
from config import put_data
from config import load_data

from core import github_parse_reps
from core import clone_github_rep


class Os:
    """This is parent class of other classes such as GnuLinux or Windows
    """
    def __init__(self):
        self.data = check_filling_of_data()

    def introduce_program(self):
        txt = """
        Welocme to getgit! I Hope that you will enjoy this program!
        From people to people!
        """
        print(txt)

    def ask_git_version_service(self):
        txt = "Choose git service that you use:\n"
        gits = ("github", "gitlab")
        return txt, gits

    def wishes(self):
        wishes = "\nEverythins is ready! If yow whant change something "
        wishes += "just go to config/config.yaml and change there data"
        print(wishes)


class GnuLinux(Os):
    """Child of Os class
    Cli interface for GnuLinux systems
    """
    def __init__(self):
        from simple_term_menu import TerminalMenu

        super().__init__()

        if self.data == 0:
            """If user start this program for the first time
            """
            self.introduce_program()
            self.menu_title = ask_git_version_service()[0]
            self.menu_items = ask_git_version_service()[1]
        if self.data == 1:
            """If user have the data in $HOME/.config/config.yaml
            """
            menu_title = "Choose repository to clone\n"
            data_config = load_data()
            if data_config["service"] == "github":
                menu_items = github_parse_reps(data_config["nickname"])
        terminal_menu = TerminalMenu(menu_entries=menu_items,
                                    title=menu_title,)
        menu_entry_index = terminal_menu.show()

        if self.data == 0:
            git_service = ask_git_version_service()[1][menu_entry_index]
            nickname = input("Write you nickname: ")

            put_data(git_service, nickname)

            self.wishes()
        if self.data == 1:
            rep_name = menu_items[menu_entry_index]
            clone_github_rep(data_config["nickname"], rep_name)


if __name__ == "__main__":
    from sys import platform
    if platform == "win32":
        pass
    if platform == "linux":
        GnuLinux()