from argparse import ArgumentParser
from .constants import PROG_NAME


def parse_args():
    args = ArgumentParser(prog=PROG_NAME)
    args.add_argument('-s', '--service', type=str)
    args.add_argument('-n', '--nickname', type=str)
    args.add_argument('-r', '--rep-name', type=str)
    args.add_argument('-p', '--port', type=str)
    args.add_argument('-c', '--cfg-info')
    return args.parse_args()
