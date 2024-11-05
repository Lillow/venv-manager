from manager_venv.manager_venv import ManagerVenv
from utils.terminal_utils import clean_screen
from menu_manager.menu_options import MenuOptions
from menu_django import options_django as op
from manager_django.manager_django import ManagerDjango


def menu_django(venv: ManagerVenv, manage_django: ManagerDjango):
    clean_screen()

    menu_options_django = MenuOptions(
        f"""
█▀▄ ░░█ ▄▀█ █▄░█ █▀▀ █▀█   █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀
█▄▀ █▄█ █▀█ █░▀█ █▄█ █▄█   █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█

\033[1m{manage_django._name}\033[0m
        """,
        {
            1: ("Run Server", lambda: op.runserver(manage_django)),
            2: ("Start App", lambda: op.start_app(manage_django)),
            3: ("Run project command", lambda: op.run_project_command(manage_django)),
        },
    )
    menu_options_django.choice()
