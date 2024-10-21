import platform
import subprocess
from manager.manager import Manager


class ManagerVenv(Manager):
    """Manages virtual environments (venv) using the Manager class.

    This class allows for the creation of virtual environments, installation of libraries,
    execution of commands within the venv, and checking for installed libraries.

    Attributes:
        __platform (str): The operating system platform (e.g., 'Windows', 'Linux').
        __venv_path (str): The path to the venv activation script.
    """

    def __init__(self, venv_name: str = "venv") -> None:
        """Initialize the ManagerVenv with a virtual environment name.

        Args:
            venv_name (str): Name of the virtual environment (default is "venv").
        """
        super().__init__(venv_name)
        self.__platform: str = platform.system()
        self.__venv_path: str = self.__get_venv_path()

    def _create(self) -> bool:
        """Create a virtual environment if it doesn't exist.

        Returns:
            bool: True if the venv was created successfully, False otherwise.
        """
        output = True
        if not self._exists_dir():
            try:
                complete_command: str = f"python -m venv {self._name}"

                print("Creating or finding venv...")

                result: subprocess.CompletedProcess[str] = subprocess.run(
                    complete_command, shell=True, capture_output=True, text=True
                )

                if result.returncode == 0:
                    print(f"Virtual environment '{self._name}' created successfully.")
                    output = True
                else:
                    print(f"Error creating virtual environment: {result.stderr}")
                    output = False
            except Exception as e:
                print(f"Error: {e}")
                output = False
        return output

    def __get_venv_path(self) -> str:
        """Get the path to the venv activation script based on the OS.

        Returns:
            str: The path to the activation script.
        """
        if self.__platform == "Windows":
            return f"{self._dir_path}\\Scripts"
        return f"{self._dir_path}/bin/"

        # Does not work in other directories
        # if self.__platform == "Windows":
        #     return f".\\{self._dir_path}\\Scripts"
        # return f"./{self._dir_path}/bin/"

    def execute_venv_command(self, command: str) -> list[str]:
        """Execute a command within the activated virtual environment.

        Args:
            command (str): The command to run in the venv.

        Returns:
            list[str]: The standard output and error of the command.
        """
        complete_command: str = f"{self.__venv_path}\\activate && {command}"
        output: list[type[str]] = [str]
        try:
            result: subprocess.CompletedProcess[str] = subprocess.run(
                complete_command, shell=True, capture_output=True, text=True
            )
            output.append(result.stdout.strip())
            output.append(result.stderr.strip())

        except Exception as e:
            output.append(f"\nAn error occurred while executing the command: {e}")
        output = output[1:]
        return output

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

    def check_library(self, library_name: str) -> bool:
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
