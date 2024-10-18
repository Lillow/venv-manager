from abc import ABCMeta, abstractmethod
from typing import Callable


class ManagerMenu(metaclass=ABCMeta):
    def __init__(self, banner: str = None) -> None:
        if banner:
            print(banner, "\n")
