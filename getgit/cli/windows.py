from config import check_filling_of_data
from config import put_data
from config import load_data

from core import github_parse_reps
from core import clone_github_rep

from general import introduce_program
from general import ask_git_version_service
from general import wishes


# TODO: make for i ... in function and use it in
# choose_git_version_service_cli and choose_reps_cli
def choose_git_version_service_cli():
    services = ask_git_version_service()[1]
    for i in range(len(services)):
        print("\t{}. {}".format(i+1, services[i]))
    service_num = input("\nChoose git version: ")
    service_num = int(service_num)-1
    return services[service_num]

def choose_reps_cli(reps):
    """Allow user choose reps and return number of it
    Reps have list type of data
    """
    for i in range(len(reps)):
        print("\t{}. {}".format(i+1, reps[i]))
    reps_num = input("\nChoose rep: ")
    reps_num = int(reps_num)-1
    return reps[reps_num]
    


def main():
    data = check_filling_of_data()
    if data == 0:
        """If user start this program for the first time
        """
        introduce_program()
        git_service = choose_git_version_service_cli()
        nickname = input("Write your nickname: ")

        put_data(git_service, nickname)
        wishes()

    if data == 1:
        """If user have the data in .config/config.yaml
        """
        print("\tChoose repository to clone\n")
        data_config = load_data()
        if data_config["service"] == "github":
            reps = github_parse_reps(data_config["nickname"])
        rep_name = choose_reps_cli(reps)
        clone_github_rep(data_config["nickname"], rep_name)
