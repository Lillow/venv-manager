from pathlib import Path
from abc import ABCMeta, abstractmethod


class Manager(metaclass=ABCMeta):

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
