from pathlib import Path
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
                print("Installing Django...")
                print(self._venv.install_library("django")[0][32:43])
                self._venv.install_library("django")
            if not self._exists_dir():
                command: str = f"python -m django startproject {self.__str__()}"
                if self._venv.execute_venv_command(command):
                    print(f"Django project '{self.__str__()}' created successfully!")
                    output = True
                else:
                    print(f"Failed to create Django project '{self.__str__()}'.")
                    output = False
        except Exception as e:
            print(f"Error creating Django project '{self.__str__()}': {e}")
            output = False
        return output

    def execute_project_command(self, command) -> list[type[str]]:
        AND = ";"
        if self._venv._platform == "Windows":
            AND = "&&"
        output: list[type[str]] = self._venv.execute_venv_command(
            f"cd {self._dir_path} {AND} python manage.py {command} {AND} cd .. {AND} exit"
        )
        return output

    def runserver(self) -> list[type[str]]:
        AND = ";"
        if self._venv._platform == "Windows":
            AND = "&&"
        output: list[type[str]] = self._venv.run_venv_command(
            f"python {self._dir_path}\\manage.py runserver {AND} exit"
        )
        return output

    def start_app(self, app_name: str) -> None:
        if not self._exists_dir(app_name):
            self.execute_project_command(f"startapp {app_name}")
        settings: str = f"{self._name}\\settings.py"
        if self._exists_file(settings):
            self._add_app(file_path=settings, new_app=app_name)

    def _add_app(self, file_path: str, new_app: str) -> None:
        content: str = self._get_content(file_path)

        if self._exists_content(content, f"'{new_app}'") or self._exists_content(
            content, f'"{new_app}"'
        ):
            print(f"The app '{new_app}' is already in INSTALLED_APPS.")
            return

        new_content: str = self._change_content(
            content, new_app, "INSTALLED_APPS = [", "]"
        )

        self._update_content(file_path, new_content)
