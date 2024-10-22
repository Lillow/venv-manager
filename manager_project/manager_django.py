from manager_project.manager_project import ManagerProject
from manager_venv.manager_venv import ManagerVenv


class ManagerDjango(ManagerProject):
    """Manages Django projects by extending the ManagerProject class.

    Handles the creation of Django projects within a specified virtual environment.
    """

    def __init__(self, venv: ManagerVenv, project_name: str) -> None:
        """Initialize the ManagerDjango with a virtual environment and project name.

        Args:
            venv (ManagerVenv): The ManagerVenv instance managing the virtual environment.
            project_name (str): The name of the Django project.
        """
        super().__init__(venv, project_name)

    def _create_project(self) -> bool:
        """Create a Django project within the virtual environment.

        Checks if Django is installed, installs it if necessary, and creates a new
        Django project if the project directory does not exist.

        Returns:
            bool: True if the Django project was created successfully, False otherwise.
        """
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

    def execute_project_command(self, command):
        operator = ";"
        if self._venv._platform == "Windows":
            operator = "&&"
        output = self._venv.execute_venv_command()(
            f"python .\\{self._name}\\manage.py {command} {operator} exit"
        )
        return output

    def runserver(self) -> list[type[str]]:
        operator = ";"
        if self._venv._platform == "Windows":
            operator = "&&"
        output = self._venv.run_venv_command(
            f"python .\\{self._name}\\manage.py runserver {operator} exit"
        )
        return output
