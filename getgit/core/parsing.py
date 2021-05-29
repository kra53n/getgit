# parse web information

from requests import exceptions as requests_exceptions
from requests import get as requests_get
from bs4 import BeautifulSoup

from sys import exit


def request_html(path):
    '''Check existing of page. If page not exist function
    return False
    '''
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
        from pathlib import Path
        home = str(Path.home())

        message = "You put incorrect nickname, "
        message += "go to {}/.config/getgit".format(home)
        message += " and change in config.yaml `nickname`"
        print(message)
        exit()
    return soup

def github_parse_reps(nickname):
    """
    Catch repositories from Github page of user.
    And return list of repositories`s name
    """
    url = "https://github.com/" + str(nickname) + "?tab=repositories"
    html_doc = request_html(url)
    soup = load_soup(url)

    reps = []
    for tag in soup.find_all("h3"):
        rep = tag.find("a").string
        rep = rep.replace("\n", "")
        rep = rep.replace(" ", "")
        reps.append(rep)
    return reps
