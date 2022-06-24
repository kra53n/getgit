from .cli import cli
from .args import parse_args
from .clone import clone_rep
from .wwyaml import put_data
from .parse import get_config_data


def main():
    args = parse_args()

    if all(fargs := (args.service_name, args.name, args.rep_name, args.port_name)):
        clone_rep(*fargs)
    elif all(fargs := (args.service_name, args.name, args.rep_name)):
        clone_rep(*fargs)
    elif all(fargs := (args.service_name, args.name)):
        put_data(*fargs)
    elif args.rep_name:
        data = get_config_data()
        clone_rep(data['service'], data['nickname'], args.rep_name)
    else:
        cli()
