"""Cli interface for getgit"""

from config import check_filling_of_data
from config import put_data
from config import load_data

from core import github_parse_reps
from core import clone_github_rep

class Os:
    """This is parent class of other classes such as GnuLinux or Windows
    """
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
        self.introduce_program()


if __name__ == "__main__":
    from sys import platform
    if platform == "win32":
        pass
    if platform == "linux":
        GnuLinux()