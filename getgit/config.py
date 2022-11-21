from pathlib import Path


PROG_NAME = 'getgit'
PROG_VERS = '0.1.7'

USER_CONFIG_DIR = Path.home() / '.config/getgit'
USER_CONFIG_NAME = 'config.yaml'
PARSE_CONFIG_PATH = Path(__file__).parent / 'config/parse.yaml'
