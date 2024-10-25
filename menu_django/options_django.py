from manager_django.manager_django import ManagerDjango
from utils.terminal_utils import print_line, pause_and_clear

def runserver(project: ManagerDjango) -> None:
    print_line(project.runserver())
    pause_and_clear()