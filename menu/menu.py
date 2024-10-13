from typing import Any
from manager_venv.manager_venv import ManagerVenv
from manager_project.manager_django import ManagerDjango
from manager_project.manager_flask import ManagerFlask
from menu.options import Options
from utils.terminal_utils import pause_and_clear, clean_screen, print_line


def menu() -> None:
    """Display the main menu after creating a virtual environment."""
    print(
        """
▀█░█▀ █▀▀ █▀▀▄ ▀█░█▀ 　 █▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀▀ █▀▀ █▀▀█ 
░█▄█░ █▀▀ █░░█ ░█▄█░ 　 █░▀░█ █▄▄█ █░░█ █▄▄█ █░▀█ █▀▀ █▄▄▀ 
░░▀░░ ▀▀▀ ▀░░▀ ░░▀░░ 　 ▀░░░▀ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀░▀▀
        \n"""
    )
    venv = create_venv()
    show_main_menu(venv)


def show_main_menu(venv: ManagerVenv) -> None:
    """Show the main menu with project management and library options.

    Args:
        venv (ManagerVenv): Virtual environment manager object.
    """
    clean_screen()
    banner = """
█░█ █▀▀ █▄░█ █░█   █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀
▀▄▀ ██▄ █░▀█ ▀▄▀   █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█"""

    main_menu = Options(
        {
            1: ("Create project", lambda: create_project_options(venv)),
            2: ("Install library", lambda: install_library(venv)),
            3: ("List libraries", lambda: list_library(venv)),
            4: ("Execute command", lambda: execute_command(venv)),
        },
        banner,
    )
    main_menu.choice()
    clean_screen()


def create_project_options(venv: ManagerVenv) -> None:
    """Show menu for creating Django or Flask projects.

    Args:
        venv (ManagerVenv): Virtual environment manager object.
    """
    clean_screen()
    banner = """
█▀█ █▀█ █▀█ ░░█ █▀▀ █▀▀ ▀█▀   █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀
█▀▀ █▀▄ █▄█ █▄█ ██▄ █▄▄ ░█░   █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█"""

    project_menu = Options(
        {
            1: ("Create Django project", lambda: create_project(venv, "Django")),
            2: ("Create Flask project", lambda: create_project(venv, "Flask")),
        },
        banner,
    )
    project_menu.choice()
    clean_screen()


def create_venv() -> ManagerVenv:
    """Create a virtual environment with a user-specified name or a default name.

    Returns:
        ManagerVenv: The created virtual environment manager object.
    """
    venv_name: str = input("Virtual environment name (default venv): ")
    return ManagerVenv(venv_name) if venv_name else ManagerVenv()


def create_project(venv: ManagerVenv, project_type: str) -> ManagerVenv:
    """Create a Django or Flask project based on the selected option.

    Args:
        venv (ManagerVenv): Virtual environment manager object.
        project_type (str): The type of project to create ("Django" or "Flask").

    Returns:
        ManagerVenv: The manager of the created project.
    """
    project_name: str = input("Project name: ")
    print("Creating...\n")

    if project_type == "Django":
        project = ManagerDjango(venv, project_name)
    elif project_type == "Flask":
        project = ManagerFlask(venv, project_name)
    else:
        project = None

    pause_and_clear()
    return project


def install_library(venv: ManagerVenv) -> None:
    """Prompt the user to install a library in the virtual environment.

    Args:
        venv (ManagerVenv): Virtual environment manager object.
    """
    clean_screen()
    library_name: str = input("Library name: ")
    print("Installing...\n")
    print_line(venv.install_library(library_name))
    pause_and_clear()


def list_library(venv: ManagerVenv) -> None:
    """List all installed libraries in the virtual environment.

    Args:
        venv (ManagerVenv): Virtual environment manager object.
    """
    clean_screen()
    print("Finding...\n")
    print_line(venv.list_library())
    pause_and_clear()


def execute_command(venv: ManagerVenv) -> None:
    """Execute a custom command inside the virtual environment.

    Args:
        venv (ManagerVenv): Virtual environment manager object.
    """
    clean_screen()
    command: str = input("Command: ")
    print("\nRunning...\n")
    print_line(venv.execute_venv_command(command))
    pause_and_clear()
