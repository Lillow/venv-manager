from manager_venv.manager_venv import ManagerVenv
from utils.terminal_utils import clean_screen
from menu_manager.menu_options import MenuOptions
from menu_flask import options_flask as op
from manager_django.manager_django import ManagerDjango


def menu_flask(venv: ManagerVenv, manage_flask: ManagerDjango):
    clean_screen()

    menu_options_flask = MenuOptions(
        """
█▀▀ █░░ ▄▀█ █▀ █▄▀   █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀
█▀░ █▄▄ █▀█ ▄█ █░█   █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█
        """,
        {1: ("Run server", lambda: op.runserver(manage_flask))},
    )
    menu_options_flask.choice()
