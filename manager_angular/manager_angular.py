from manager_project.manager_project import ManagerProject
import subprocess
import sys


class ManagerAngular(ManagerProject):
    def __init__(self, project_name: str = "angular_project") -> None:
        super().__init__("kill_venv", project_name)

    def _create_project(self) -> None:
        if self._check_node():
            if not self._check_angular():
                print("\nInstalling angular cli...\n")
                self._install_angular()
                print(self._angular_version())
            print("\nCreating angular project...\n")
            print(self._start_project())

    def _check_node(self) -> bool:
        return True if self._execute_command("node --version")[0][0] == "v" else False

    def _check_angular(self) -> bool:
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

    def _start_project(self) -> list[type[str]]:
        return self._execute_command(f"ng new {self._name} --skip-install")
