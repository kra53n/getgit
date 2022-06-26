from .cli import cli
from .args import parse_args
from .clone import clone_rep
from .wwyaml import put_data
from .parse import get_config_data


def main():
    args = parse_args()

    # NOTE: rename service_name to service
    # NOTE: rename name to nickname
    if all(fargs := (args.service_name, args.name, args.rep_name, args.port_name)):
        clone_rep(*fargs)
    elif all(fargs := (args.service_name, args.name, args.rep_name)):
        clone_rep(*fargs)
    elif all(fargs := (args.service_name, args.name)):
        put_data(*fargs)
    elif any((args.service_name, args.name, args.rep_name)):
        data = get_config_data()
        if args.service_name:
            put_data(args.service_name, data['nickname'], port=data['port'])
        if args.name:
            put_data(data['service'], args.name, port=data['port'])
        if args.rep_name:
            clone_rep(data['service'], data['nickname'], args.rep_name)
    else:
        cli()
