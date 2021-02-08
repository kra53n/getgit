# parse web information


from requests import get as requests_get
from bs4 import BeautifulSoup

from sys import exit


def request_html(path):
    '''Check existing of page. If page not exist function
    return False
    '''
    html_doc = requests_get(path)
    if html_doc.status_code != 200:
        return False
    return html_doc.text


def github_parse_reps(nickname):
    '''Catch repositories from Github page of user.
    And return list of repositories`s name
    '''
    path = "https://github.com/" + str(nickname) + "?tab=repositories"
    html_doc = request_html(path)
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

    reps = []
    for tag in soup.find_all("h3"):
        rep = tag.find("a").string
        rep = rep.replace("\n", "")
        rep = rep.replace(" ", "")
        reps.append(rep)
    return reps
