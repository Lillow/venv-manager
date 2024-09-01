from abc import ABCMeta, abstractmethod
from venv_creator.venv_creator import VenvCreator


class ProjectCreator(metaclass=ABCMeta):

    def __init__(self, venv: VenvCreator, project_name: str) -> None:
        self._project_name = project_name
        self.venv = venv
        self.create_project()

    @abstractmethod
    def create_project(self) -> bool:
        pass
