from ast import main
import os
import platform
import subprocess
import sys
import venv

import venv_creator


class VenvCreator:
    def __init__(self, venv_name: str = "venv") -> None:
        self._venv_name: str = venv_name.strip().replace(" ", "_")
        self._platform: str = platform.system()
        self.__venv_path: str = self._get_venv_path(venv_name)
        self.is_created = True
        self.is_created: bool = (
            self.__create_venv() if not os.path.exists(venv_name) else True
        )

    def _get_venv_path(self, venv_name: str) -> str:
        if self._platform == "Windows":
            return f".\\{venv_name}\\Scripts"
        return f"./{venv_name}/bin/"

    def __create_venv(self) -> bool:
        try:
            complete_command = f"python -m venv {self._venv_name}"

            print("Creating or finding venv...")

            result = subprocess.run(
                complete_command, shell=True, capture_output=True, text=True
            )

            if result.returncode == 0:
                print(f"Virtual environment '{self._venv_name}' created successfully.")
                return True
            else:
                print(f"Error creating virtual environment: {result.stderr}")
                return False
        except Exception as e:
            print(f"Error creating the virtual environment: {e}")
            return False

    def execute_venv_command(self, command: str) -> list[str]:
        complete_command = f"{self.__venv_path}\\activate && {command}"
        ret = False
        output: list[type[str]] = [str]
        try:
            result = subprocess.run(
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
        if output[0] != '':
            file_path = os.path.join(os.getcwd(), "requirements.txt")
            with open(file_path, 'a') as f:
                f.write(f"{library_name}\n")
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

    def __str__(self) -> str:
        return self._venv_name
