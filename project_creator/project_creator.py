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

    def _directory_creator(self, dirs: list):
        for directory in dirs:
            directory = self._base_dir / directory
            directory.mkdir(parents=True, exist_ok=True)

    def _file_creator(self, file_name, file_content):
        (self._base_dir / file_name).write_text(file_content)

    def __str__(self) -> str:
        name = self._project_name
        return name