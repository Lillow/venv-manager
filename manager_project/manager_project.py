from abc import ABCMeta, abstractmethod
from manager.manager import Manager
from manager_venv.manager_venv import ManagerVenv


class ManagerProject(Manager, metaclass=ABCMeta):
    def __init__(self, venv: ManagerVenv, project_name: str) -> None:
        self.__venv: ManagerVenv = venv
        super().__init__(project_name)

    def _create(self) -> bool:
        return self._create_project()

    @abstractmethod
    def _create_project(self) -> bool:
        pass

    @property
    def _venv(self) -> ManagerVenv:
        return self.__venv
