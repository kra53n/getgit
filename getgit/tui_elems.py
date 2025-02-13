from typing import Iterable


def get_num_from_user(title: str, error_message: str, num_range: range) -> int:
    while not (num := input(title)).isdigit() or not int(num) in num_range:
        print(error_message)
    return int(num)


def select_option(title: str, opts: Iterable[str]) -> str:
    for idx, opt in enumerate(opts, 1):
        print(f'\t{idx}. {opt}')
    print()
    idx = get_num_from_user(title, f'Put digit from 1 to {len(opts)}', range(1, len(opts) + 1))
    return opts[idx - 1]
