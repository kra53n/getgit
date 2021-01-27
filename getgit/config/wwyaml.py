"""wwyaml - work with yaml"""

from yaml import load
from yaml import FullLoader
from yaml import dump


PATH_CONF_FILE = "config/config.yaml"


def load_data():
    """Return parsed data from config.yaml
    """
    with open(PATH_CONF_FILE) as f:
        data = load(f, Loader=FullLoader)
    return data

def put_data(service, nickname):
    """Put service(github, gitlab, ...) and nickname inot config.yaml
    """
    data = {"service": service, "nickname": nickname}
    with open(PATH_CONF_FILE, "w") as f:
        dump(data, f)

def check_filling_of_data():
    """If service and nickname in config.yaml exist then return 1.
    Otherwise return 0
    """
    data = load_data()
    if (data["service"] == None) and (data["nickname"] == None):
        return 0
    return 1
