# parse web information

from requests import exceptions as requests_exceptions
from requests import get as requests_get
from bs4 import BeautifulSoup
from pathlib import Path
from sys import exit


def request_html(path):
    """
    Check existing of page. If page not exist function
    return False
    """
    try:
        html_doc = requests_get(path)
    except requests_exceptions.ConnectionError:
        print("You lost your internet connection!")
        exit()

    if html_doc.status_code != 200:
        return False
    return html_doc.text


def load_soup(url):
    """
    Return soup(or exception)
    """
    html_doc = request_html(url)
    try:
        soup = BeautifulSoup(html_doc, "html.parser")
    except TypeError:
        '''If user have incorrect nickname'''
        config_dir = Path.home() / ".config/getgit"
        message = f"You put incorrect nickname, " \
                  f"go to {config_dir}" \
                  f" and change in config.yaml `nickname`"
        print(message)
        exit()
    return soup


def github_parse_reps(nickname: str):
    """
    Catch repositories from Github page of user.
    And return list of repositories`s name
    """
    url = f"https://github.com/{nickname}?tab=repositories"
    soup = load_soup(url)

    reps = []
    for tag in soup.find_all("h3"):
        rep = tag.find("a").string
        rep = rep.replace("\n", "")
        rep = rep.replace(" ", "")
        reps.append(rep)
    return reps


def notabug_parse_reps(nickname):
    """
    Catch repositories from Notabug page of user.
    And return list of repositories`s name
    """
    url = f"https://notabug.org/{nickname}"
    soup = load_soup(url)

    reps = []
    for block in soup.find_all("a"):
        try:
            if "name" in block["class"]:
                reps.append(block.string)
        except KeyError:
            continue
    return reps
