import subprocess
from manager.manager import Manager


class ManagerVenv(Manager):
    """Manages virtual environments (venv) using the Manager class.

    This class allows for the creation of virtual environments, installation of libraries,
    execution of commands within the venv, and checking for installed libraries.

    Attributes:
        _platform (str): The operating system platform (e.g., 'Windows', 'Linux').
        __venv_path (str): The path to the venv activation script.
    """

    def __init__(self, venv_name: str = "venv") -> None:
        """Initialize the ManagerVenv with a virtual environment name.

        Args:
            venv_name (str): Name of the virtual environment (default is "venv").
        """
        super().__init__(venv_name)
        self.__venv_path: str = self.__get_venv_path()

    def _create(self) -> None:
        """Create a virtual environment if it doesn't exist.

        Returns:
            bool: True if the venv was created successfully, False otherwise.
        """
        if not self._exists_dir():
            try:
                complete_command: str = f"python -m venv {self._name}"

                print("Creating or finding venv...")

                result: list[type[str]] = self._execute_command(complete_command)

                if result[2] == 0:
                    print(f"Virtual environment '{self._name}' created successfully.")
                    self._is_created = True
                    return
                else:
                    print(f"Error creating virtual environment: {result[1]}")
                    self._is_created = False
                    return
            except Exception as e:
                print(f"Error: {e}")
                self._is_created = False

    def __get_venv_path(self) -> str:
        """Get the path to the venv activation script based on the OS.

        Returns:
            str: The path to the activation script.
        """
        if self._platform == "Windows":  # Se o caminho não for assim no exe da erro!!!
            return f"{self._dir_path}\\Scripts"
        return f"{self._dir_path}/bin/"

    def execute_venv_command(self, command: str) -> list[type[str]]:
        """Execute a command within the activated virtual environment.

        Args:
            command (str): The command to run in the venv.

        Returns:
            list[str]: The standard output and error of the command.
        """
        complete_command: str = f"{self.__venv_path}\\activate && {command}"
        return self._execute_command(complete_command)

    def run_venv_command(self, command: str) -> list[type[str]]:
        complete_command: str = f"{self.__venv_path}\\activate && {command}"
        return self._run_command(complete_command)

    def install_library(self, library_name: str) -> list[str]:
        """Install a library using pip in the virtual environment.

        Args:
            library_name (str): The name of the library to install.

        Returns:
            list[str]: The output of the pip install command.
        """
        output: list[str] = self.execute_venv_command(f"pip install {library_name}")
        if output[0] != "":
            self._create_file("request.txt", library_name)
        return output

    def is_library_installed(self, library_name: str) -> bool:
        """Check if a library is installed in the virtual environment.

        Args:
            library_name (str): The name of the library to check.

        Returns:
            bool: True if the library is installed, False otherwise.
        """
        output: list[str] = self.execute_venv_command(
            f"python -m {library_name} --version"
        )
        if output[0] == "":
            return False
        return True

    def list_library(self) -> list[str]:
        """List all installed libraries in the virtual environment.

        Returns:
            list[str]: The output of the 'pip list' command.
        """
        return self.execute_venv_command("pip list")
