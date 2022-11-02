import requests
from yaml import safe_load as yaml_load
from bs4 import BeautifulSoup
from pathlib import Path
from sys import exit

from .config import USER_CONFIG_DIR, PARSE_CONFIG_PATH
from .wwyaml import UserData


def get_parse_config_data(path: Path = PARSE_CONFIG_PATH) -> dict:
    return yaml_load(path.read_text())


def get_url(data: UserData) -> str:
    return get_parse_config_data()[data.service]['url'].replace('nickname', data.nickname)


def request_html(path):
    """
    Check existing of page. If page not exist function
    return False
    """
    try:
        html_doc = requests.get(path)
    except requests.exceptions.ConnectionError:
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
                  f"go to {USER_CONFIG_DIR}" \
                  f" and change in config.yaml `nickname`"
        print(message)
        exit()
    return soup


def parse_reps(data: UserData) -> list | None:
    config = get_parse_config_data(PARSE_CONFIG_PATH)[data.service]

    if 'attrs' not in config.keys():
        return

    url = get_url(data)
    tags = get_soup(url).find_all(config['tag'])
    rep_names = []

    for tag in tags:
        if 'attrs' in config.keys():
            for key, value in config['attrs'].items():
                if not (key in tag.attrs and tag.attrs[key] == value):
                    break
            else:
                rep_names.append(tag.string.replace('\n', '').lstrip())

    return rep_names
