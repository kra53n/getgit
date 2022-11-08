from os import system
from .parse import get_parse_config_data
from .wwyaml import UserData, create_file
from .config import BASE_DIR


def clone_rep(data: UserData, rep_name: str):
    port = f'-{data.port}' if data.port else ''
    message = get_parse_config_data()[data.service]['rep'+port]
    message = message.replace('nickname', data.nickname)
    message = message.replace('rep_name', rep_name)
    print(message)
    system(f'git clone {message}')
    file = BASE_DIR / ".repos"
    if not file.exists():
        create_file(BASE_DIR, ".repos")
    file.write_text(f"{data.nickname}/{rep_name}")
