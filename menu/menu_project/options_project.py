from manager_venv.manager_venv import ManagerVenv
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
                return ManagerDjango(venv, project_name)
                _create_and_clear()
                break
            case "2":
                return ManagerFlask(venv, project_name)
                _create_and_clear()
                break
            case "3":
                return None
                _create_and_clear()
                break


def _create_and_clear() -> None:
    pause_and_clear()
    print("Creating or find project...\n")
