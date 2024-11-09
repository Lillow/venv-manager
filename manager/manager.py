import subprocess
import platform
from pathlib import Path
from abc import ABCMeta, abstractmethod
from unittest.mock import patch


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
        self._platform: str = platform.system()
        self._is_created: bool = False

    @abstractmethod
    def _create(self) -> bool:
        """Abstract method to handle directory creation or other setup tasks.

        Returns:
            bool: True if creation was successful, False otherwise.
        """
        pass

    def _execute_command(self, command) -> list[type[str]]:
        output: list[type[str]] = [str]
        try:
            process: subprocess.CompletedProcess[str] = subprocess.run(
                command, shell=True, capture_output=True, text=True
            )
            output.append(process.stdout.strip())
            output.append(process.stderr.strip())
            output.append(process.returncode)

        except Exception as e:
            output.append(f"\nAn error occurred while executing the command: {e}")
        output = output[1:]
        return output

    def _run_command(self, command: str) -> list[type[str]]:
        output: list[type[str]] = [str]
        try:
            process = None
            args = []
            shell = False

            match platform.system():
                case "Windows":
                    args = ["start", "cmd", "/k", command]
                    shell = True
                case "Linux":
                    args = [
                        "gnome-terminal",
                        "--",
                        "bash",
                        "-c",
                        command + "; exec bash",
                    ]
                case "Darwin":
                    args = ["open", "-a", "Terminal", command]
                case _:
                    output.append("Operating system not supported.")
                    return output
            process = subprocess.Popen(args=args, shell=shell)
        except Exception as e:
            print(f"\nAn error occurred while run the command: {e}")
        output.append("Running command...\n")
        output = output[1:]
        return output

    def _exists_dir(self, dir_path: str = "") -> bool:
        """Check if the managed directory exists.

        Returns:
            bool: True if the directory exists, False otherwise.
        """
        dir_path = self._dir_path / dir_path
        return dir_path.exists()

    def _exists_file(self, file_path: str = "") -> bool:
        file_path = self._dir_path / file_path
        return file_path.exists() and file_path.is_file()

    def _exists_content(self, entire_content: str, content: str) -> bool:
        if content in entire_content:
            return True
        return False

    def _get_content(self, file_path: Path) -> str:
        file_path = self._dir_path / file_path
        return file_path.read_text()

    def _change_content(
        self, entire_content: str, new_content: str, init_content: str, end_content: str
    ) -> str:
        i_init: int = entire_content.find(init_content)
        if i_init == -1:
            print("Initial content not found.")
            return ""
        i_end: int = entire_content.find(end_content, i_init)

        new_content: str = (
            entire_content[:i_end] + f"    '{new_content}',\n" + entire_content[i_end:]
        )
        return new_content

    def _update_content(self, file_path: str, new_content: str) -> None:
        file_path = self._dir_path / file_path
        file_path.write_text(new_content)

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
