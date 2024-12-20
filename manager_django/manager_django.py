from pathlib import Path
from manager_project.manager_project import ManagerProject
from manager_venv.manager_venv import ManagerVenv


class ManagerDjango(ManagerProject):
    """Manages Django projects by extending the ManagerProject class.

    Handles the creation of Django projects within a specified virtual environment.
    """

    def __init__(self, venv: ManagerVenv, project_name: str = "project_django") -> None:
        """Initialize the ManagerDjango with a virtual environment and project name.

        Args:
            venv (ManagerVenv): The ManagerVenv instance managing the virtual environment.
            project_name (str): The name of the Django project.
        """
        super().__init__(venv, project_name)

    def _create_project(self) -> None:
        """Create a Django project within the virtual environment.

        Checks if Django is installed, installs it if necessary, and creates a new
        Django project if the project directory does not exist.

        Returns:
            bool: True if the Django project was created successfully, False otherwise.
        """
        try:
            if not self._venv.is_library_installed("django"):
                print("Installing Django...")
                print(self._venv.install_library("django")[0][32:43])
                self._venv.install_library("django")
            if not self._exists_dir():
                command: str = f"python -m django startproject {self.__str__()}"
                if self._venv.execute_venv_command(command):
                    print(f"Django project '{self.__str__()}' created successfully!")
                    self._is_created = True
                    return
                else:
                    print(f"Failed to create Django project '{self.__str__()}'.")
                    self._is_created = False
                    return
        except Exception as e:
            print(f"Error creating Django project '{self.__str__()}': {e}")
            self._is_created = False

    def venv_runserver(self) -> list[type[str]]:
        return self.run_venv_django_command("runserver")

    def start_app(self, app_name: str) -> None:
        if not self._exists_dir(app_name):
            self.execute_venv_django_command(f"startapp {app_name}")
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

    def execute_venv_django_command(self, command) -> list[type[str]]:
        complete_command: str = f"python manage.py {command}"
        return self._execute_venv_project_command(complete_command)

    def run_venv_django_command(self, command) -> list[type[str]]:
        complete_command: str = f"python manage.py {command}"
        return self._run_venv_project_command(complete_command)
