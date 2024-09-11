from venv_creator.venv_creator import VenvCreator as Venv
from project_creator.django_creator import DjangoCreator as Django
from project_creator.flask_creator import FlaskCreator as Flask
from project_creator.project_creator import ProjectCreator as Project
from time import sleep


def menu() -> None:
    print(
        """
    █▀█ █▀█ █▀█ ░░█ █▀▀ █▀▀ ▀█▀   █▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀█ █▀█
    █▀▀ █▀▄ █▄█ █▄█ ██▄ █▄▄ ░█░   █▄▄ █▀▄ ██▄ █▀█ ░█░ █▄█ █▀▄
        """
    )
    venv = create_venv()
    option(venv)


def option(venv: Venv) -> None:
    while True:
        print("\n1 - Create project")
        print("2 - Install library")
        print("3 - List libraries")
        print("4 - Execute command")
        print("0 - Leave")
        option = input("\nChoose an option: ")

        match option:
            case "1":
                create_project_options(venv)
            case "2":
                install_library(venv)
            case "3":
                list_library(venv)
            case "4":
                execute_command(venv)
                limpar_tela()
            case "0":
                print("Leaving...")
                sleep(2)
                break


def create_project_options(venv: Venv):
    while True:
        print("\n1 - Create Django project")
        print("2 - Create Flask project")
        print("3 - Create Custom project")
        print("0 - Leave")
        option = input("\nChoose an option: ")

        match option:
            case "1":
                project = create_project(venv, "Django")
                print(project)
                break
            case "2":
                project = create_project(venv, "Flask")
                print(project)
                break
            case "3":
                project = create_project(venv, "Custom")
                break
            case "0":
                print("Leaving...")
                sleep(2)
                break


def create_venv() -> Venv:
    venv_name = input("Virtual environment name (default venv): ")
    print("Creating or finding venv...\n")
    if venv_name == "":
        venv = Venv()
    else:
        venv = Venv(venv_name)
    return venv


def create_project(venv: Venv, project_tipe: str) -> Project:
    project_name = input("Project name: ")
    project = None
    print("creating..\n")
    if project_tipe == "Django":
        project = Django(venv, project_name)
    elif project_tipe == "Flask":
        project = Flask(venv, project_name)
    elif project_tipe == "Custom":
        project = None
    return project


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
