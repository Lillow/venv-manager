from project_creator.project_creator import ProjectCreator


class DjangoCreator(ProjectCreator):

    def create_project(self) -> bool:
        checker = False
        try:
            if not self.venv.check_library("django"):
                self.venv.install_library("django")

            if (self.venv.execute_venv_command(f"python -m django startproject {self._project_name}")):
                checker = True
        except Exception as e:
            print(f"Erro ao criar o projeto django {self._project_name}: {e}")

        return checker
