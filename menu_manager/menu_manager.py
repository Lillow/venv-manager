from abc import ABCMeta, abstractmethod
from typing import Callable


class MenuManager(metaclass=ABCMeta):
    def __init__(self, banner: str = None) -> None:
        self._banner: str = banner


    def print_banner(self):
        if self._banner != None:
            print(self._banner, "\n")
