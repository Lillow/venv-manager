from project_creator.project_creator import ProjectCreator


class DjangoCreator(ProjectCreator):
    def _create_project(self) -> bool:
        try:
            if not self._venv.check_library("django"):
                self._venv.install_library("django")

            command = f"python -m django startproject {self._project_name}"
            if self._venv.execute_venv_command(command):
                return True
            else:
                print(f"Failed to create Django project '{self._project_name}'.")
                return False
        except Exception as e:
            print(f"Error creating Django project '{self._project_name}': {e}")
            return False
