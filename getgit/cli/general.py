def introduce_program():
    txt = """
    Welocme to getgit! I Hope that you will enjoy this program!
    From people to people!
    """
    print(txt)

def ask_git_version_service():
    txt = "Choose git service that you use:\n"
    gits = ("github", "gitlab")
    return txt, gits

def wishes():
    wishes = "\nEverythins is ready! If yow whant change something "
    wishes += "just go to config/config.yaml and change there data"
    print(wishes)