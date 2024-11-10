from manager_angular.manager_angular import ManagerAngular
from utils.terminal_utils import pause_and_clear, clean_screen, print_line


def runserver(project: ManagerAngular) -> None:
    project.runserver()
    pause_and_clear()


def run_command(project: ManagerAngular) -> None:
    clean_screen()
    command: str = input("Command: ")
    print("\nRunning...\n")
    print_line(project.run_angular_command(command))
    pause_and_clear()


def add_library(project: ManagerAngular):
    clean_screen()
    library_name: str = input("Library name: ")
    print("Installing...\n")
    print_line(project.add_library(library_name))
    pause_and_clear()
