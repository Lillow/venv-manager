from menu_organized.menu_initial import MenuInitial
from menu_organized.menu_options import MenuOptions
from menu_organized.menu_main import MenuMain
from manager_venv.manager_venv import ManagerVenv
from utils.terminal_utils import pause_and_clear, clean_screen, print_line


def menu_venv():
    menu_initial_venv = menu_venv = MenuInitial(
        """
▀█░█▀ █▀▀ █▀▀▄ ▀█░█▀ 　 █▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀▀ █▀▀ █▀▀█ 
░█▄█░ █▀▀ █░░█ ░█▄█░ 　 █░▀░█ █▄▄█ █░░█ █▄▄█ █░▀█ █▀▀ █▄▄▀ 
░░▀░░ ▀▀▀ ▀░░▀ ░░▀░░ 　 ▀░░░▀ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀░▀▀
            """,
        "Virtual environment name (default venv): ",
    )
    manager_venv: ManagerVenv = (
        ManagerVenv(menu_initial_venv.manager_name)
        if menu_initial_venv.manager_name
        else ManagerVenv()
    )
    clean_screen()

    menu_options_venv = options_venv = MenuOptions(
        """
█░█ █▀▀ █▄░█ █░█   █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀
▀▄▀ ██▄ █░▀█ ▀▄▀   █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█""",
        {
            1: ("Manage project", lambda: project_manager(manager_venv)),
            2: ("Install library", lambda: install_library(manager_venv)),
            3: ("List libraries", lambda: list_library(manager_venv)),
            4: ("Execute command", lambda: execute_command(manager_venv)),
        },
    )
    menu_options_venv.choice()
    clean_screen()

    def project_manager() -> None:
        print("Criando ou encontrando projeto")
        return True

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

    menu_venv = MenuMain(menu_initial_venv, manager_venv, menu_options_venv)
