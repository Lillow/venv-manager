from manager_flask.manager_flask import ManagerFlask
from utils.terminal_utils import print_line, pause_and_clear

def runserver(project: ManagerFlask) -> None:
    print_line(project.runserver())
    pause_and_clear()