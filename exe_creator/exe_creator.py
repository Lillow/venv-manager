import venv
from zipapp import create_archive

from click import command
from exe_create import create_executable

# from menu.menu import create_exe
from venv_creator.venv_creator import VenvCreator


class ExeCreator:
    def __init__(
        self, venv: VenvCreator, file_path: str, icon_path: str = None
    ) -> None:
        self._venv: VenvCreator = venv
        self._file_path: str = file_path
        self._icon_path: str = icon_path
        self._output = self.create_executable()

    def create_executable(self) -> list:
        output: list[str] = list()
        try:
            if not self._venv.check_library("PyInstaller"):
                self._venv.install_library("PyInstaller")
            command: str = (
                f"{self._venv.sys_executable} -m PyInstaller --onefile {self._file_path}"
            )

            if self._icon_path:
                command.extend(["--icon", self._icon_path])
            output: list[str] = self._venv.execute_venv_command(command)

        except Exception as e:
            output.append(f"Error when searching or installing PyInstaller ': {e}")
        return output
