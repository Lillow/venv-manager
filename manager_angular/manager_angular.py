from manager_project.manager_project import ManagerProject
import subprocess
import sys


class ManagerAngular(ManagerProject):
    def __init__(self, project_name: str = "angular_project") -> None:
        super().__init__("kill_venv", project_name)

    def _create_project(self) -> None:
        if self._is_node_installed():
            if not self._is_angular_installed():
                print("\nInstalling angular cli...\n")
                self._install_angular()
                print(self._angular_version())
            print("\nCreating or find angular project...\n")
        if not self._exists_dir():
            AND = ";"
            if self._platform == "Windows":
                AND = "&&"
            self._run_command(f"ng new {self._name} {AND} exit")

    def runserver(self) -> list[type[str]]:
        return self.run_angular_command(f"serve")

    def _is_node_installed(self) -> bool:
        return True if self._execute_command("node --version")[0][0] == "v" else False

    def _is_angular_installed(self) -> bool:
        try:
            int(self._angular_version()[0])
            return True
        except Exception as e:
            print(e)
            return False

    def _angular_version(self) -> type[str]:
        return self._execute_command("ng --version")[0]

    def _install_angular(self) -> list[type[str]]:
        return self._execute_command("npm install -g @angular/cli")

    def execute_angular_command(self, command: str) -> list[type[str]]:
        return self._execute_project_command(f"ng {command}")

    def run_angular_command(self, command: str) -> list[type[str]]:
        return self._run_project_command(f"ng {command}")

    def add_library(self, library_name: str) -> list[type[str]]:
        return self.run_angular_command(f" add {library_name}")
