from pathlib import Path


PROG_NAME = 'getgit'
PROG_VERS = '0.1.6'

CONFIG_DIR = Path.home() / '.config/getgit'
CONFIG_NAME = 'config.yaml'
CONFIG_PARSE_PATH = Path(__file__).parent / 'config/parse.yaml'
