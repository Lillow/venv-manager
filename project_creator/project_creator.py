from pathlib import Path
from abc import ABCMeta, abstractmethod
from venv_creator.venv_creator import VenvCreator


class ProjectCreator(metaclass=ABCMeta):

    def __init__(self, venv: VenvCreator, project_name: str) -> None:
        self._project_name = project_name
        self._venv = venv
        self._base_dir = Path(self._project_name)
        self._create_project()

    @abstractmethod
    def _create_project(self) -> bool:
        pass
