from .args import args
from .cli import cli
from .clone import clone_rep
from .wwyaml import put_data
from .parse import get_config_data


def main():
    if all(map(lambda x: x is not None, (args.service_name, args.name, args.rep_name))):
        clone_rep(args.service_name, args.name, args.rep_name)
    elif all(map(lambda x: x is not None, (args.service_name, args.name))):
        put_data(args.service_name, args.name)
    elif args.rep_name:
        data = get_config_data()
        clone_rep(data['service'], data['nickname'], args.rep_name)
    else:
        cli()


if __name__ == '__main__':
    main()
