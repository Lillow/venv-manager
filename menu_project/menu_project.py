from manager_venv.manager_venv import ManagerVenv
from menu_manager.menu_initial import MenuInitial
from menu_manager.menu_options import MenuOptions
from menu_manager.menu_main import MenuMain
from utils.terminal_utils import pause_and_clear, clean_screen, print_line
from menu_project import options_project as op
from manager_project.manager_project import ManagerProject


def menu_project(venv: ManagerVenv):
    clean_screen()
    menu_initial_project: MenuInitial = MenuInitial(
        """
▒█▀▀█ █▀▀█ █▀▀█ ░░▀ █▀▀ █▀▀ ▀▀█▀▀ 　 ▒█▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀▀ █▀▀ █▀▀█ 
▒█▄▄█ █▄▄▀ █░░█ ░░█ █▀▀ █░░ ░░█░░ 　 ▒█▒█▒█ █▄▄█ █░░█ █▄▄█ █░▀█ █▀▀ █▄▄▀ 
▒█░░░ ▀░▀▀ ▀▀▀▀ █▄█ ▀▀▀ ▀▀▀ ░░▀░░ 　 ▒█░░▒█ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀░▀▀""",
        "Python Project name: ",
    )

    clean_screen()

    project_name: str = menu_initial_project.manager_name
    manager_project: ManagerProject = op.create_project(venv, project_name)

    clean_screen()

    menu_options_project = MenuOptions(
        """
█▀█ █▀█ █▀█ ░░█ █▀▀ █▀▀ ▀█▀   █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀
█▀▀ █▀▄ █▄█ █▄█ ██▄ █▄▄ ░█░   █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█""",
        {1: ("Run server", lambda: op.runserver(manager_project))},
    )
    menu_options_project.choice()

    menu_project = MenuMain(menu_initial_project, manager_project, menu_options_project)
