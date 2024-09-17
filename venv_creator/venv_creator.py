import os
import platform
import subprocess
import sys

# import venv

# import msvcrt


class VenvCreator:
    def __init__(self, venv_name: str = "venv") -> None:
        self._venv_name: str = venv_name
        self.__system: str = platform.system()
        self.__venv_path: str = self._get_venv_path(venv_name)
        self.is_created = True
        self.is_created: bool = (
            self.__create_venv() if not os.path.exists(venv_name) else True
        )

    def _get_venv_path(self, venv_name: str) -> str:
        if self.__system == "Windows":
            return f".\\{venv_name}\\Scripts"
        return f"./{venv_name}/bin/"

    def __create_venv(self) -> bool:
        try:
            complete_command = f"{sys.executable} -m venv {self._venv_name}"

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

    def execute_venv_command(self, command: str) -> str:
        complete_command = f"{self.__venv_path}\\activate && {command}"
        ret = False
        output = str()
        try:
            result = subprocess.run(
                complete_command, shell=True, capture_output=True, text=True
            )
            output = f"""Outputs:\n{ result.stdout.strip()}
Errors:\n{result.stderr.strip()}
"""
            # print("Outputs:\n", result.stdout.strip())
            # print("Errors:\n", result.stderr.strip())
        except Exception as e:
            output += f"\nAn error occurred while executing the command: {e}"
            # print(f"\nAn error occurred while executing the command: {e}")
        return output

    def install_library(self, library_name: str) -> bool:
        return self.execute_venv_command(f"pip install {library_name}")

    def check_library(self, library_name: str) -> bool:
        return self.execute_venv_command(f"python -m {library_name} --version")

    def list_library(self) -> bool:
        print(self.execute_venv_command("pip list"))
        # return self.execute_venv_command("pip list")

    def __str__(self) -> str:
        return self._venv_name


if __name__ == "__main__":
    venv = VenvCreator()
    venv.list_library()


# def clean_screen() -> None:
#     os.system("cls" if os.name == "nt" else "clear")


# def wait_for_keypress() -> None:
#     print("\nPress any key to continue...")

#     try:
#         msvcrt.getch()
#     except Exception as e:
#         print(f"Error waiting for key press: {e}")
