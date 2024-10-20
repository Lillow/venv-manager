from manager_venv.manager_venv import ManagerVenv
from menu_organized.menu_initial import MenuInitial
from menu_organized.menu_options import MenuOptions
from menu_organized.menu_main import MenuMain
from utils.terminal_utils import pause_and_clear, clean_screen, print_line
from menu.menu_project import options_project as op


def menu_project(venv: ManagerVenv):
    clean_screen()
    menu_initial_project: MenuInitial = MenuInitial(
        """
▒█▀▀█ █▀▀█ █▀▀█ ░░▀ █▀▀ █▀▀ ▀▀█▀▀ 　 ▒█▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀▀ █▀▀ █▀▀█ 
▒█▄▄█ █▄▄▀ █░░█ ░░█ █▀▀ █░░ ░░█░░ 　 ▒█▒█▒█ █▄▄█ █░░█ █▄▄█ █░▀█ █▀▀ █▄▄▀ 
▒█░░░ ▀░▀▀ ▀▀▀▀ █▄█ ▀▀▀ ▀▀▀ ░░▀░░ 　 ▒█░░▒█ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀░▀▀""",
        "Python Project name: ",
    )

    # manager_project = ManagerProject(venv, )
    # menu_initial_project.manager_name

    clean_screen()

    menu_options_project = MenuOptions(
        """
█▀█ █▀█ █▀█ ░░█ █▀▀ █▀▀ ▀█▀   █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀
█▀▀ █▀▄ █▄█ █▄█ ██▄ █▄▄ ░█░   █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█""",
        {},
    )

    # menu_project = MenuMain(menu_initial_project, manager_project, menu_options_project)
