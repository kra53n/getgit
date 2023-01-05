from sys import argv

from .cli import cli, print_cfg_info
from .args import parse_args
from .clone import clone_rep
from .parse import parse_reps
from .config import PROG_VERS
from .wwyaml import (UserData, load_dict_to_UserData, change_UserData,
                     put_data, load_data)


def main():
    argc = len(argv)
    args = parse_args()
    user_data = change_UserData(load_data(),
                                load_dict_to_UserData(args.__dict__,UserData()))
    if argc == 1:
        cli()
    elif args.change:
        put_data(user_data)
    elif args.rep_name:
        clone_rep(user_data, args.rep_name)
    elif args.version:
        print(f'getgit {PROG_VERS}')
    elif args.cfg_info:
        print_cfg_info()
    elif args.list:
        for rep in parse_reps(user_data):
            print(rep)
    else:
        print('getgit requires `--change` flag to change settings in config')
        print('otherwise print `getgit -h` to see help')
