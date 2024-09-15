from venv_creator.venv_creator import VenvCreator as Venv
from project_creator.django_creator import DjangoCreator as Django
from project_creator.flask_creator import FlaskCreator as Flask
from project_creator.project_creator import ProjectCreator as Project
from menu.options import Options
from venv_creator.venv_creator import clean_screen
from time import sleep


def menu() -> None:
    print_banner()
    venv = create_venv()
    show_main_menu(venv)


def print_banner() -> None:
    clean_screen()
    print(
        """
    █▀█ █▀█ █▀█ ░░█ █▀▀ █▀▀ ▀█▀   █▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀█ █▀█
    █▀▀ █▀▄ █▄█ █▄█ ██▄ █▄▄ ░█░   █▄▄ █▀▄ ██▄ █▀█ ░█░ █▄█ █▀▄
        """
    )


def show_main_menu(venv: Venv) -> None:
    main_menu = Options(
        {
            1: ("Create project", lambda: create_project_options(venv)),
            2: ("Install library", lambda: install_library(venv)),
            3: ("List libraries", lambda: list_library(venv)),
            4: ("Execute command", lambda: execute_command(venv)),
        }
    )
    main_menu.choice()


def create_project_options(venv: Venv) -> None:
    project_menu = Options(
        {
            1: ("Create Django project", lambda: create_project(venv, "Django")),
            2: ("Create Flask project", lambda: create_project(venv, "Flask")),
            # 3: ("Create Custom project", lambda: create_project(venv, "Custom")),
        }
    )
    project_menu.choice()


def create_venv() -> Venv:
    venv_name = input("Virtual environment name (default venv): ")
    print("Creating or finding venv...\n")
    return Venv(venv_name) if venv_name else Venv()


def create_project(venv: Venv, project_type: str) -> Project:
    project_name = input("Project name: ")
    print("Creating...\n")
    if project_type == "Django":
        return Django(venv, project_name)
    elif project_type == "Flask":
        return Flask(venv, project_name)
    # elif project_type == "Custom":
        # return None


def install_library(venv: Venv) -> None:
    library_name = input("Library name: ")
    print("Installing...\n")
    if venv.install_library(library_name):
        print(f"Library {library_name} installed correctly")
    else:
        print(f"Library {library_name} not installed")


def list_library(venv: Venv) -> None:
    print("Finding...\n")
    if not venv.list_library():
        print("Failed to find libraries")


def execute_command(venv: Venv) -> None:
    command = input("Command: ")
    print("\nRunning...\n")
    if not venv.execute_venv_command(command):
        print("Failed to execute command")
