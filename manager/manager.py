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
        """Initialize the Manager instance with a directory name.

        Args:
            name (str): The name of the directory, formatted to remove spaces.
        """
        self._name: str = name.strip().replace(" ", "_")
        self._base_dir: Path = Path(".")
        self._dir_path: Path = self._base_dir / self._name
        self._is_created: bool = self._create()

    @abstractmethod
    def _create(self) -> bool:
        """Abstract method to handle directory creation or other setup tasks.

        Returns:
            bool: True if creation was successful, False otherwise.
        """
        pass

    def _exists_dir(self, dir_path: str = "") -> bool:
        """Check if the managed directory exists.

        Returns:
            bool: True if the directory exists, False otherwise.
        """
        dir_path = self._dir_path / dir_path
        return dir_path.exists()

    def _create_directory(self, dir_path: str = "") -> None:
        """Create a list of directories inside the managed directory.

        Args:
            directories (list[str]): List of directory names to create.
        """
        # for directory in directories:
        dir_path = self._dir_path / dir_path
        dir_path.mkdir(parents=True, exist_ok=True)

    def _create_file(self, file_path: str, file_content: str) -> None:
        """Create a file with the given content inside the managed directory.

        Args:
            file_name (str): Name of the file to create.
            file_content (str): Content to write to the file.
        """
        file_path = self._dir_path / file_path
        file_path.write_text(file_content)

    def __str__(self) -> str:
        """Return the name of the managed directory.

        Returns:
            str: Directory name.
        """
        return self._name
