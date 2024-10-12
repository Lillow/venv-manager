from manager_project.manager_project import ManagerProject
from manager_venv.manager_venv import ManagerVenv


class ManagerDjango(ManagerProject):
    def __init__(self, venv: ManagerVenv, project_name: str) -> None:
        super().__init__(venv, project_name)

    def _create_project(self) -> bool:
        output = True
        try:
            if not self._venv.check_library("django"):
                self._venv.install_library("django")
            if not self._exists_dir():
                command: str = f"python -m django startproject {self.__str__()}"
                if self._venv.execute_venv_command(command):
                    print(f"Jango project '{self.__str__()}' created successfully!")
                    output = True
                else:
                    print(f"Failed to create Django project '{self.__str__()}'.")
                    output = False
        except Exception as e:
            print(f"Error creating Django project '{self.__str__()}': {e}")
            output = False
        return output
