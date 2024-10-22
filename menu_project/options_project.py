from manager_venv.manager_venv import ManagerVenv
from manager_project.manager_project import ManagerProject
from manager_project.manager_django import ManagerDjango
from manager_project.manager_flask import ManagerFlask
from utils.terminal_utils import pause_and_clear, clean_screen


def create_project(
    venv: ManagerVenv, project_name: str
) -> ManagerDjango | ManagerFlask:
    while True:
        clean_screen()
        print(
            """
𝙋𝙧𝙤𝙟𝙚𝙘𝙩 𝙏𝙮𝙥𝙚

    1 - Django project
    2 - Flask project
    3 - Others
    """
        )
        option: str = input("\nChoose an option: ")
        match option:
            case "1":
                _create_and_clear()
                return ManagerDjango(venv, project_name)
            case "2":
                _create_and_clear()
                return ManagerFlask(venv, project_name)
            case "3":
                _create_and_clear()
                return None


def _create_and_clear() -> None:
    # pause_and_clear()
    print("Creating or find project...\n")


def runserver(project: ManagerProject):
    print(project.runserver())
    pause_and_clear()
