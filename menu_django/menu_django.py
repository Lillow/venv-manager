from manager_venv.manager_venv import ManagerVenv
from utils.terminal_utils import clean_screen
from menu_manager.menu_options import MenuOptions
from menu_django import options_django as op
from manager_django.manager_django import ManagerDjango


def menu_django(venv: ManagerVenv, manage_django: ManagerDjango):
    clean_screen()

    menu_options_django = MenuOptions(
        """
█▀▄ ░░█ ▄▀█ █▄░█ █▀▀ █▀█   █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀
█▄▀ █▄█ █▀█ █░▀█ █▄█ █▄█   █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█
        """,
        {1: ("Run server", lambda: op.runserver(manage_django))},
    )
    menu_options_django.choice()
