import os
import platform
import subprocess


class VenvCreator:
    def __init__(self, venv_name: str = "venv") -> None:
        self._venv_name = venv_name
        self.__system = platform.system()
        self.__venv_path = self._get_venv_path(venv_name)
        self.is_created = (
            self.__create_venv() if not os.path.exists(venv_name) else True
        )

    def _get_venv_path(self, venv_name: str) -> str:
        if self.__system == "Windows":
            return f".\\{venv_name}\\Scripts"
        return f"./{venv_name}/bin/"

    def __create_venv(self) -> bool:
        try:
            complete_command = f"python -m venv {self._venv_name}"
            result = subprocess.run(
                complete_command, shell=True, capture_output=True, text=True
            )
            if result.returncode == 0:
                print(f"Ambiente virtual '{self._venv_name}' criado com sucesso.")
                return True
            else:
                print(f"Erro ao criar o ambiente virtual: {result.stderr}")
                return False
        except Exception as e:
            print(f"Erro ao criar o ambiente virtual: {e}")
            return False

    def execute_venv_command(self, command: str) -> bool:
        complete_command = f"{self.__venv_path}\\activate && {command}"
        try:
            result = subprocess.run(
                complete_command, shell=True, capture_output=True, text=True
            )
            print("Saída:\n", result.stdout.strip())
            print("Erros:\n", result.stderr.strip())
            return result.returncode == 0
        except Exception as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")
            return False

    def install_library(self, library_name: str) -> bool:
        return self.execute_venv_command(f"pip install {library_name}")

    def check_library(self, library_name: str) -> bool:
        return self.execute_venv_command(f"python -m {library_name} --version")

    def list_library(self) -> bool:
        return self.execute_venv_command("pip list")

    def __str__(self) -> str:
        return self._venv_name


def clean_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")
