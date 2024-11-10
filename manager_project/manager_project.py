from abc import ABCMeta, abstractmethod
from manager.manager import Manager
from manager_venv.manager_venv import ManagerVenv


class ManagerProject(Manager, metaclass=ABCMeta):
    """Abstract base class for managing projects with virtual environments.

    This class extends the Manager class to handle project-specific tasks,
    such as project directory creation and managing virtual environments.

    Attributes:
    __venv (ManagerVenv): The virtual environment manager for the project.
    """

    def __init__(self, venv: ManagerVenv, project_name: str) -> None:
        """Initialize the ManagerProject with a virtual environment and project name.

        Args:
            venv (ManagerVenv): The ManagerVenv instance for managing the project's virtual environment.
            project_name (str): The name of the project.
        """
        self._venv: ManagerVenv = venv
        super().__init__(project_name)

    @abstractmethod
    def _create_project(self) -> bool:
        """Abstract method to handle project creation.

        This method must be implemented by subclasses to define the steps
        for creating the project.

        Returns:
            bool: True if the project was created successfully, False otherwise.
        """
        pass

    def _create(self) -> bool:
        """Create the project by calling the _create_project method.

        Returns:
            bool: True if the project was created successfully, False otherwise.
        """
        return self._create_project()

    def venv_runserver() -> list[type[str]]:
        pass

    def _execute_project_command(self, command) -> list[type[str]]:
        AND = ";"
        if self._venv._platform == "Windows":
            AND = "&&"
        output: list[type[str]] = self.execute_command(
            f"cd {self._dir_path} {AND} {command} {AND} cd .. {AND} exit"
        )
        return output

    def _run_project_command(self, command) -> list[type[str]]:
        AND = ";"
        if self._platform == "Windows":
            AND = "&&"
        output: list[type[str]] = self._run_command(
            f"cd {self._dir_path} {AND} {command} {AND} cd .. {AND} exit"
        )
        return output

    def _execute_venv_project_command(self, command) -> list[type[str]]:
        AND = ";"
        if self._venv._platform == "Windows":
            AND = "&&"
        output: list[type[str]] = self._venv.execute_venv_command(
            f"cd {self._dir_path} {AND} {command} {AND} cd .. {AND} exit"
        )
        return output

    def _run_venv_project_command(self, command) -> list[type[str]]:
        AND = ";"
        if self._venv._platform == "Windows":
            AND = "&&"
        output: list[type[str]] = self._venv.run_venv_command(
            f"cd {self._dir_path} {AND} {command} {AND} cd .. {AND} exit"
        )
        return output
