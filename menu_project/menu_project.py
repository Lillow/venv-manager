from manager_venv.manager_venv import ManagerVenv
from menu_manager.menu_initial import MenuInitial
from menu_manager.menu_options import MenuOptions
from utils.terminal_utils import clean_screen
from menu_project import options_project as op


def menu_project(venv: ManagerVenv):
    clean_screen()
    menu_initial_project: MenuInitial = MenuInitial(
        """

▒█▀▀█ ▒█▀▀█ ▒█▀▀▀█ ░░░▒█ ▒█▀▀▀ ▒█▀▀█ ▀▀█▀▀   ▒█▀▄▀█ ░█▀▀█ ▒█▄░▒█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀█ 
▒█▄▄█ ▒█▄▄▀ ▒█░░▒█ ░▄░▒█ ▒█▀▀▀ ▒█░░░ ░▒█░░   ▒█▒█▒█ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ▒█░▄▄ ▒█▀▀▀ ▒█▄▄▀ 
▒█░░░ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄█ ▒█▄▄▄ ▒█▄▄█ ░▒█░░   ▒█░░▒█ ▒█░▒█ ▒█░░▀█ ▒█░▒█ ▒█▄▄█ ▒█▄▄▄ ▒█░▒█
        """,
        "Python Project name (default project): ",
    )

    clean_screen()

    project_name: str = menu_initial_project.manager_name

    clean_screen()

    menu_options_project = MenuOptions(
        """
█▀█ █▀█ █▀█ ░░█ █▀▀ █▀▀ ▀█▀   █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀
█▀▀ █▀▄ █▄█ █▄█ ██▄ █▄▄ ░█░   █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█
        """,
        {
            1: ("Django", lambda: op.create_project(venv, project_name, "django")),
            2: ("Flask", lambda: op.create_project(venv, project_name, "flask")),
            # 3: ("Others", lambda: op.create_project(project_name)),
        },
    )
    menu_options_project.choice()
