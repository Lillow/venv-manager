from pathlib import Path
from abc import ABCMeta, abstractmethod
import os


class Manager(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.__name: str = name.strip().replace(" ", "_")
        self.__base_dir: str = os.getcwd()
        self.__is_created = True
        self.__is_created: bool = self._create()

    @abstractmethod
    def _create(self) -> bool:
        pass

    @property
    def _base_dir(self) -> str:
        return self.__base_dir
    
    @property
    def _is_created(self) -> bool:
        return self.__is_created

    def __str__(self) -> str:
        return self.__name

    # def _create_directories(self, directories: list[str]) -> None:
    #     for directory in directories:
    #         dir_path = self._base_dir / directory
    #         dir_path.mkdir(parents=True, exist_ok=True)

    # def _create_file(self, file_name: str, file_content: str) -> None:
    #     (self._base_dir / file_name).write_text(file_content)
