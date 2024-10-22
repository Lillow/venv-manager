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

    def _create(self) -> bool:
        """Create the project by calling the _create_project method.

        Returns:
            bool: True if the project was created successfully, False otherwise.
        """
        return self._create_project()

    @abstractmethod
    def _create_project(self) -> bool:
        """Abstract method to handle project creation.

        This method must be implemented by subclasses to define the steps
        for creating the project.

        Returns:
            bool: True if the project was created successfully, False otherwise.
        """
        pass

    def runserver() -> list[type[str]]:
        pass
