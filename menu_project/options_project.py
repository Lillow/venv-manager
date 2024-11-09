from typing import Self
from manager_venv.manager_venv import ManagerVenv
from manager_project.manager_project import ManagerProject
from manager_django.manager_django import ManagerDjango
from manager_flask.manager_flask import ManagerFlask
from menu_django.menu_django import menu_django
from menu_flask.menu_flask import menu_flask
from utils.terminal_utils import pause_and_clear


def create_project(
    venv: ManagerVenv, project_name: str, type_project: str = ""
) -> ManagerProject:
    print("\nCreating or finding project...\n")
    match type_project:
        case "django":
            manager_project = (
                ManagerDjango(venv, project_name)
                if project_name
                else ManagerDjango(venv)
            )
            manager_project._create()
            pause_and_clear()
            menu_django(venv, manager_project)
        case "flask":
            manager_project = (
                ManagerFlask(venv, project_name) if project_name else ManagerFlask(venv)
            )
            manager_project._create()
            pause_and_clear()
            menu_flask(venv, manager_project)
        case _:
            manager_project = None
