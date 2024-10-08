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

    def _create_directories(self, directories: list[str]) -> None:
        for directory in directories:
            dir_path = self._base_dir / directory
            dir_path.mkdir(parents=True, exist_ok=True)

    def _create_file(self, file_name: str, file_content: str) -> None:
        (self._base_dir / file_name).write_text(file_content)

    def __str__(self) -> str:
        return self._project_name
