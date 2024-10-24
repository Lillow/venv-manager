from manager_venv.manager_venv import ManagerVenv
from manager_project.manager_project import ManagerProject
from manager_django.manager_django import ManagerDjango
from manager_flask.manager_flask import ManagerFlask
from utils.terminal_utils import pause_and_clear, print_line


def create_project(
    venv: ManagerVenv, project_name: str, type_project: str = ""
) -> ManagerProject:
    print("\nCreating or finding project...\n")
    match type_project:
        case "django":
            manager_project = ManagerDjango(venv, project_name)
            pause_and_clear()
            # menu_jango(manager_project)
        case "flask":
            manager_project = ManagerFlask(venv, project_name)
            pause_and_clear()
            # menu_flask(manager_project)
        case _:
            manager_project = None


def runserver(project: ManagerProject) -> None:
    print_line(project.runserver())
    pause_and_clear()
