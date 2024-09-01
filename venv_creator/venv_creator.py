import os
import platform
import subprocess
import venv


class VenvCreator:

    def __init__(self, venv_name: str = "venv") -> None:

        self._venv_name = venv_name
        self.__system = platform.system()
        self.is_created = self.__create_venv() if not os.path.exists(venv_name) else True
        # self.__venv_path = f".\\{venv_name}\\Scripts" if self.__system == "Windows" else f"./{venv_name}/bin/"
        self.__venv_path = f".\\{venv_name}\\Scripts" if self.__system == "Windows" else f"./{venv_name}/bin/"

    def __create_venv(self) -> bool:

        try:
            venv.create(self._venv_name, with_pip=True)
        except Exception as e:
            print(f"Erro ao criar o ambiente virtual: {e}")
            return False
        print(f"Ambiente virtual '{self._venv_name}' criado com sucesso.")
        return True

    def execute_venv_command(self, command: str) -> bool:
        complete_command = f"{self.__venv_path}\\activate && {command} && deactivate"
        checker = False
        result = None
        try:
            result = subprocess.run(
                complete_command, shell=True, capture_output=True, text=True)
            # if result.stdout
            if(result.stdout != ''):
                checker = True
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        print("Saída:\n", result.stdout)
        print("Erros:\n", result.stderr)
        return checker

    def install_library(self, library_name: str) -> bool:
        return self.execute_venv_command(f"pip install {library_name}")

    def check_library(self, library_name: str) -> bool:
        return self.execute_venv_command(f"python -m {library_name} --version")

    def list_library(self) -> bool:
        return self.execute_venv_command(f"pip list")
    