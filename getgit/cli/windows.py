from config import check_filling_of_data
from config import put_data
from config import load_data

from core import github_parse_reps
from core import clone_github_rep

from .general import introduce_program
from .general import ask_git_version_service


def choose_git_version_service_cli():
    services = ask_git_version_service[1]
    for i in range(len(services)):
        print("{}. {}".format(i+1, services[i]))
    service_num = input("Choose git version: ")
    service_num = int(service) - 1
    return services[service]

def main():
    print("Hello!")
    data = check_filling_of_data()
    if data == 0:
        """If user start this program for the first time
        """
        introduce_program()
        choose_git_version_service_cli()
