from manager_django.manager_django import ManagerDjango
from utils.terminal_utils import print_line, pause_and_clear, clean_screen


def runserver(project: ManagerDjango) -> None:
    print_line(project.venv_runserver())
    pause_and_clear()


def start_app(project: ManagerDjango) -> None:
    app_name = input("\nApp name: ")
    print("\nCreating or finding app...\n")
    project.start_app(app_name)
    print("App created successfully.\n")
    pause_and_clear()


def run_django_project_command(project: ManagerDjango) -> None:
    clean_screen()
    command: str = input("Command: ")
    print("\nRunning...\n")
    project.run_django_project_command(command)
    pause_and_clear()
