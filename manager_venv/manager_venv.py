import platform
import subprocess
from manager.manager import Manager


class ManagerVenv(Manager):
    def __init__(self, venv_name: str = "venv") -> None:
        super().__init__(venv_name)
        self.__platform: str = platform.system()
        self.__venv_path: str = self.__get_venv_path()

    def _create(self) -> bool:
        output = True
        if not self._exists_dir():
            try:
                complete_command: str = f"python -m venv {self.__str__()}"

                print("Creating or finding venv...")

                result: subprocess.CompletedProcess[str] = subprocess.run(
                    complete_command, shell=True, capture_output=True, text=True
                )

                if result.returncode == 0:
                    print(
                        f"Virtual environment '{self._venv_name}' created successfully."
                    )
                    output = True
                else:
                    print(f"Error creating virtual environment: {result.stderr}")
                    output = False
            except Exception as e:
                print(f"Error: {e}")
                output = False
        return output

    def __get_venv_path(self) -> str:
        if self.__platform == "Windows":
            return f"{self._dir_path}\\Scripts"
        return f"{self._dir_path}/bin/"

    def execute_venv_command(self, command: str) -> list[str]:
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
        output: list[str] = self.execute_venv_command(f"pip install {library_name}")
        # if output[0] != "":
        #     self._create_file("request.txt", library_name)
        return output

    def check_library(self, library_name: str) -> bool:
        output: list[str] = self.execute_venv_command(
            f"python -m {library_name} --version"
        )
        if output[0] == "":
            return False
        return True

    def list_library(self) -> list[str]:
        return self.execute_venv_command("pip list")
