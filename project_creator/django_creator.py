from project_creator.project_creator import ProjectCreator


class DjangoCreator(ProjectCreator):

    def _create_project(self) -> bool:
        checker = False
        try:
            if not self._venv.check_library("django"):
                self._venv.install_library("django")

            if (self._venv.execute_venv_command(f"python -m django startproject {self._project_name}")):
                checker = True
        except Exception as e:
            print(f"Erro ao criar o projeto django {self._project_name}: {e}")

        return checker
