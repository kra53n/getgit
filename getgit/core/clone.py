from os import system


def clone_github_rep(nickname, rep_name):
    print("git clone https://github.com/{}/{}".format(nickname, rep_name))
    system("git clone https://github.com/{}/{}".format(nickname, rep_name))

def clone_notabug_rep(nickname, rep_name):
    print("git clone https://notabug.org/{}/{}".format(nickname, rep_name))
    system("git clone https://notabug.org/{}/{}".format(nickname, rep_name))
