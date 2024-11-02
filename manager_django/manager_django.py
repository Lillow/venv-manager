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
        AND = ";"
        if self._venv._platform == "Windows":
            AND = "&&"
        output = self._venv.execute_venv_command(
            f"cd {self._dir_path} {AND} python manage.py {command} {AND} cd .. {AND} exit"
        )
        return output

    def runserver(self) -> list[type[str]]:
        AND = ";"
        if self._venv._platform == "Windows":
            AND = "&&"
        output = self._venv.run_venv_command(
            f"python {self._dir_path}\\manage.py runserver {AND} exit"
        )
        return output

    def start_app(self, app_name) -> list[type[str]]:
        if not self._exists_dir(app_name):
            self.execute_project_command(f"startapp {app_name}")
        settings = f"{self._name}\\settings.py"
        if self._exists_file(settings):
            self._add_app(file_path=settings, new_app=app_name)

    def _add_app(self, file_path: str, new_app: str) -> None:
        # Obter o caminho completo do arquivo
        file_path = self._dir_path / file_path

        # Ler o conteúdo do arquivo
        content = file_path.read_text()

        # Verificar se o app já está em INSTALLED_APPS
        if new_app in content:
            print(f"O app '{new_app}' já está em INSTALLED_APPS.")
            return

        # Procurar o índice do fechamento da lista INSTALLED_APPS
        apps_start = content.find("INSTALLED_APPS = [")
        if apps_start == -1:
            print("A lista INSTALLED_APPS não foi encontrada.")
            return

        # Encontrar a posição de fechamento da lista
        closing_bracket_index = content.find("]", apps_start)

        # Inserir o novo app antes do colchete de fechamento
        updated_content = (
            content[:closing_bracket_index]
            + f"    '{new_app}',\n"
            + content[closing_bracket_index:]
        )

        # Escrever o conteúdo atualizado de volta no arquivo
        file_path.write_text(updated_content)
        print(
            f"O app '{new_app}' foi adicionado ao final de INSTALLED_APPS com sucesso."
        )
