from manager_angular.manager_angular import ManagerAngular
from utils.terminal_utils import pause_and_clear


def runserver(project: ManagerAngular) -> None:
    project.runserver()
    pause_and_clear()
