from pathlib import Path


def ask_user_rep_name():
    pass


def ask_user_for_his_info():
    pass


def save_user_info_to_config(user_info):
    pass


def dl_rep(rep_name: str):
    user_data = load_data()
    clone_rep(user_data, rep_name)


def get_info_about_user_from_config(config_path: Path = USER_CONFIG_DIR / filename):
    pass


def dl_all():
    """
    Download all visible repositories of user
    """
    user_data = load_data()
    reps_names = parse_reps(user_data)
    for rep_name in reps_names:
        clone_rep(user_data, rep_name)
