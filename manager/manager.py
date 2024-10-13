from pathlib import Path
from abc import ABCMeta, abstractmethod


class Manager(metaclass=ABCMeta):
    """Abstract base class for managing directories and files.

    Provides functionality for directory creation, file writing, and
    checking if a directory exists. Subclasses should implement the `_create` method.

    Attributes:
        _name (str): Manager name, formatted without spaces.
        _base_dir (Path): Base working directory.
        _dir_path (Path): Full path to the managed directory.
        _is_created (bool): Indicates if the directory was successfully created.
    """

    def __init__(self, name: str) -> None:
        self._name: str = name.strip().replace(" ", "_")
        self._base_dir: Path = Path.cwd()
        self._dir_path: Path = self._base_dir / self.__str__()
        self._is_created: bool = self._create()

    @abstractmethod
    def _create(self) -> bool:
        pass

    def _exists_dir(self) -> bool:
        return self._dir_path.exists()

    def _create_directories(self, directories: list[str]) -> None:
        for directory in directories:
            dir_path = self._dir_path / directory
            dir_path.mkdir(parents=True, exist_ok=True)

    def _create_file(self, file_name: str, file_content: str) -> None:
        (self._dir_path / file_name).write_text(file_content)

    def __str__(self) -> str:
        return self._name
