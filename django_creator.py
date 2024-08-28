from venv_creator.venv_creator import VenvCreator

class DjangoCreator:
    def __init__(self, project_name: str, venv: VenvCreator = any) -> None:
        self._project_name = project_name
        self.venv = venv
        self.create_project()

    def create_project(self):
        checker = False
        try:
            if not self.venv.check_library("django"):
                self.venv.install_library("django")
            
            if(self.venv.execute_venv_command(f"python -m django startproject {self._project_name}")):
                checker = True
        except Exception as e:
            print(f"Erro ao criar o projeto django {self._project_name}: {e}")

        return checker