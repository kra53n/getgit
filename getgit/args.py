from argparse import ArgumentParser
from .config import PROG_NAME


def parse_args():
    args = ArgumentParser(prog=PROG_NAME)
    args.add_argument('-v', '--version', action='store_true', help='print getgit version')
    args.add_argument('--change', action='store_true', help='requires for settings changing')
    args.add_argument('-s', '--service', type=str, help='set the service like github, notabut, ...')
    args.add_argument('-n', '--nickname', type=str, help='set the nickname of current service')
    args.add_argument('-r', '--rep-name', type=str, help='set the repository')
    args.add_argument('-p', '--port', type=str, help='set the port like https, ssh, ...')
    args.add_argument('-c', '--cfg-info', action='store_true', help='print config information')
    args.add_argument('-l', '--list', action='store_true', help='print list of repositories')
    return args.parse_args()
