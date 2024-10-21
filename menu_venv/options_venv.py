from manager_venv.manager_venv import ManagerVenv
from utils.terminal_utils import pause_and_clear, clean_screen, print_line
from menu_project.menu_project import menu_project


def project_manager(venv: ManagerVenv) -> None:
    menu_project(venv)


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
