from argparse import ArgumentParser
from .constants import PROG_NAME


def parse_args():
    args = ArgumentParser(prog=PROG_NAME)
    args.add_argument('-s', '--service-name', help='git service name', type=str)
    args.add_argument('-p', '--port-name', help='service port', type=str)
    args.add_argument('-n', '--name', help='profile name', type=str)
    args.add_argument('-r', '--rep-name', help='repository name', type=str)
    return args.parse_args()
