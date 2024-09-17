from tabnanny import check
from venv_creator.venv_creator import VenvCreator
from project_creator.django_creator import DjangoCreator
from project_creator.flask_creator import FlaskCreator
from project_creator.project_creator import ProjectCreator
from menu.options import Options
from utils.terminal_utils import pause_and_clear, clean_screen


def menu() -> None:
    print_banner()
    venv = create_venv()
    show_main_menu(venv)


def print_banner() -> None:
    print(
        """
    █▀█ █▀█ █▀█ ░░█ █▀▀ █▀▀ ▀█▀   █▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀█ █▀█
    █▀▀ █▀▄ █▄█ █▄█ ██▄ █▄▄ ░█░   █▄▄ █▀▄ ██▄ █▀█ ░█░ █▄█ █▀▄
        """
    )


def show_main_menu(venv: VenvCreator) -> None:
    clean_screen()
    main_menu = Options(
        {
            1: ("Create project", lambda: create_project_options(venv)),
            2: ("Install library", lambda: install_library(venv)),
            3: ("List libraries", lambda: list_library(venv)),
            4: ("Execute command", lambda: execute_command(venv)),
        }
    )
    main_menu.choice()
    clean_screen()


def create_project_options(venv: VenvCreator) -> None:
    clean_screen()
    project_menu = Options(
        {
            1: ("Create Django project", lambda: create_project(venv, "Django")),
            2: ("Create Flask project", lambda: create_project(venv, "Flask")),
            # 3: ("Create Custom project", lambda: create_project(venv, "Custom")),
        }
    )
    project_menu.choice()
    clean_screen()


def create_venv() -> VenvCreator:
    venv_name = input("Virtual environment name (default venv): ")
    print("Creating or finding venv...\n")
    return VenvCreator(venv_name) if venv_name else VenvCreator()


def create_project(venv: VenvCreator, project_type: str) -> ProjectCreator:
    project_name: str = input("Project name: ")
    print("Creating...\n")
    if project_type == "Django":
        return DjangoCreator(venv, project_name)
    elif project_type == "Flask":
        return FlaskCreator(venv, project_name)
    # elif project_type == "Custom":
    # return None


def install_library(venv: VenvCreator) -> None:
    clean_screen()
    library_name = input("Library name: ")
    print("Installing...\n")
    print_line(venv.install_library(library_name))
    pause_and_clear()


def list_library(venv: VenvCreator) -> None:
    clean_screen()
    print("Finding...\n")
    print_line(venv.list_library())
    pause_and_clear()


def execute_command(venv: VenvCreator) -> None:
    clean_screen()
    command = input("Command: ")
    print("\nRunning...\n")
    print_line(venv.execute_venv_command(command))
    pause_and_clear()


def print_line(output):
    for item in output:
        print(item, "\n")
