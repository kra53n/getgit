# parse web information


from requests import get as requests_get
from bs4 import BeautifulSoup


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
    path = "https://github.com/" + nickname + "?tab=repositories"
    html_doc = request_html(path)
    soup = BeautifulSoup(html_doc, "html.parser")

    reps = []
    for tag in soup.find_all("h3"):
        rep = tag.find("a").string
        rep = rep.replace("\n", "")
        rep = rep.replace(" ", "")
        reps.append(rep)
    return reps
