from simple_term_menu import TerminalMenu

from config import check_filling_of_data
from config import put_data
from config import load_data

from core import github_parse_reps
from core import clone_github_rep

from .general import introduce_program
from .general import ask_git_version_service


def main():
    data = check_filling_of_data()
    if data == 0:
        """If user start this program for the first time
        """
        introduce_program()
        menu_title = ask_git_version_service()[0]
        menu_items = ask_git_version_service()[1]
    if data == 1:
        """If user have the data in config/config.yaml
        """
        menu_title = "Choose repository to clone\n"
        data_config = load_data()
        if data_config["service"] == "github":
            menu_items = github_parse_reps(data_config["nickname"])

    terminal_menu = TerminalMenu(menu_entries=menu_items,
                                 title=menu_title,)
    menu_entry_index = terminal_menu.show()

    if data == 0:
        git_service = ask_git_version_service()[1][menu_entry_index]
        nickname = input("Write your nickname: ")

        put_data(git_service, nickname)

        wishes = "\nEverythins is ready! If yow whant change something "
        wishes += "just go to config/config.yaml and change there data"
        print(wishes)
    if data == 1:
        rep_name = menu_items[menu_entry_index]
        clone_github_rep(data_config["nickname"], rep_name)
