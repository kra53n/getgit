from argparse import ArgumentParser
from .constants import PROG_NAME


args = ArgumentParser(prog=PROG_NAME)
args.add_argument('-s', '--service-name', help='git service name', type=str)
args.add_argument('-n', '--name', help='profile name', type=str)
args.add_argument('-r', '--rep-name', help='repository name', type=str)
args = args.parse_args()
