from menu_manager.menu_initial import MenuInitial
from menu_manager.menu_options import MenuOptions
from manager_venv.manager_venv import ManagerVenv
from utils.terminal_utils import pause_and_clear, clean_screen, print_line
from menu_venv import options_venv as op


def menu_venv() -> None:
    clean_screen()
    menu_initial_venv: MenuInitial = MenuInitial(
        """
▒█░░▒█ ▒█▀▀▀ ▒█▄░▒█ ▒█░░▒█   ▒█▀▄▀█ ░█▀▀█ ▒█▄░▒█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ 
░▒█▒█░ ▒█▀▀▀ ▒█▒█▒█ ░▒█▒█░   ▒█▒█▒█ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ▒█░▄▄ ▒█▀▀▀ ▒█▄▄▀ 
░░▀▄▀░ ▒█▄▄▄ ▒█░░▀█ ░░▀▄▀░   ▒█░░▒█ ▒█░▒█ ▒█░░▀█ ▒█░▒█ ▒█▄▄█ ▒█▄▄▄ ▒█░▒█
            """,
        "Virtual environment name (default venv): ",
    )
    manager_venv: ManagerVenv = (
        ManagerVenv(menu_initial_venv.manager_name)
        if menu_initial_venv.manager_name
        else ManagerVenv()
    )
    clean_screen()

    menu_options_venv: MenuOptions = MenuOptions(
        """
█░█ █▀▀ █▄░█ █░█   █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀
▀▄▀ ██▄ █░▀█ ▀▄▀   █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█
        """,
        {
            1: ("Manage project", lambda: op.project_manager(manager_venv)),
            2: ("Install library", lambda: op.install_library(manager_venv)),
            3: ("List libraries", lambda: op.list_library(manager_venv)),
            4: ("Execute command", lambda: op.execute_command(manager_venv)),
        },
    )
    menu_options_venv.choice()
    clean_screen()
