from ast import Return
from pathlib import Path
from abc import ABCMeta, abstractmethod
import os


class Manager(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.__name: str = name.strip().replace(" ", "_")
        self.__base_dir: str = os.getcwd()
        self.__dir_path: str = f"{self.__base_dir}\\{self.__str__()}"
        self.__is_created: bool = self._create()

    @abstractmethod
    def _create(self) -> bool:
        pass

    @property
    def _dir_path(self) -> str:
        return self.__dir_path

    @property
    def _is_created(self) -> bool:
        return self.__is_created

    def _exists_dir(self) -> bool:
        return os.path.exists(self.__str__())

    def _create_directories(self, directories: list[str]) -> None:
        for directory in directories:
            dir_path = Path(self._dir_path) / directory
            dir_path.mkdir(parents=True, exist_ok=True)

    def _create_file(self, file_name: str, file_content: str) -> None:
        (Path(self._dir_path) / file_name).write_text(file_content)

    def __str__(self) -> str:
        return self.__name
