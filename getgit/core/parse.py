# parse web information
# author: Krai53n
# date of creating: 24.01.21


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


def github_parse_reps(html_doc):
    '''Catch repositories from Github of user
    '''
    soup = BeautifulSoup(html_doc, "html.parser")
