from requests import exceptions as requests_exceptions
from requests import get as requests_get
from yaml import safe_load as yaml_load
from bs4 import BeautifulSoup
from pathlib import Path
from sys import exit

from constants import CONFIG_DIR, CONFIG_PARSE_PATH


def get_config_data(path: Path = CONFIG_PARSE_PATH) -> dict:
    return yaml_load(path.read_text())


def get_url(service: str, nickname: str) -> str:
    return get_config_data()[service]['url'].replace('nickname', nickname)


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


def get_soup(url):
    """
    Return soup(or exception)
    """
    html_doc = request_html(url)
    try:
        soup = BeautifulSoup(html_doc, "html.parser")
    except TypeError:
        # if user have incorrect nickname
        message = f"You put incorrect nickname, " \
                  f"go to {CONFIG_DIR}" \
                  f" and change in config.yaml `nickname`"
        print(message)
        exit()
    return soup


def parse_reps(service: str, path: str) -> list | None:
    """
    service - git service name
    path - url path with git repositories
    """
    data = get_config_data(CONFIG_PARSE_PATH)[service]

    if 'attrs' not in data.keys():
        return

    tags = get_soup(path).find_all(data['tag'])
    rep_names = []

    for tag in tags:
        if 'attrs' in data.keys():
            for key, value in data['attrs'].items():
                if not (key in tag.attrs and tag.attrs[key] == value):
                    break
            else:
                rep_names.append(tag.string.replace('\n', '').lstrip())

    return rep_names
