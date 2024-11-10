from menu_manager.menu_initial import MenuInitial
from menu_manager.menu_options import MenuOptions
from utils.terminal_utils import clean_screen, pause_and_clear
from manager_angular.manager_angular import ManagerAngular
from menu_angular import options_angular as op


def menu_angular() -> None:
    clean_screen()
    menu_initial_angular: MenuInitial = MenuInitial(
        """
░█▀▀█ ▒█▄░▒█ ▒█▀▀█ ▒█░▒█ ▒█░░░ ░█▀▀█ ▒█▀▀█   ▒█▀▄▀█ ░█▀▀█ ▒█▄░▒█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ 
▒█▄▄█ ▒█▒█▒█ ▒█░▄▄ ▒█░▒█ ▒█░░░ ▒█▄▄█ ▒█▄▄▀   ▒█▒█▒█ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ▒█░▄▄ ▒█▀▀▀ ▒█▄▄▀ 
▒█░▒█ ▒█░░▀█ ▒█▄▄█ ░▀▄▄▀ ▒█▄▄█ ▒█░▒█ ▒█░▒█   ▒█░░▒█ ▒█░▒█ ▒█░░▀█ ▒█░▒█ ▒█▄▄█ ▒█▄▄▄ ▒█░▒█""",
        "Angular project name (default angular_project): ",
    )
    manager_angular: ManagerAngular = (
        ManagerAngular(menu_initial_angular.manager_name)
        if menu_initial_angular.manager_name
        else ManagerAngular()
    )
    manager_angular._create_project()
    clean_screen()

    menu_options_angular: MenuOptions = MenuOptions(
        f"""
▄▀█ █▄░█ █▀▀ █░█ █░░ ▄▀█ █▀█   █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀
█▀█ █░▀█ █▄█ █▄█ █▄▄ █▀█ █▀▄   █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█
            
\033[1m{manager_angular._name}\033[0m
            """,
        {
            1: ("Run Server", lambda: op.runserver(manager_angular)),
            2: ("Add library", lambda: op.add_library(manager_angular)),
            # 3: ("List libraries", lambda: op.list_library(manager_angular)),
            3: ("Run command", lambda: op.run_command(manager_angular)),
        },
    )
    menu_options_angular.choice()
    clean_screen()
