from manager_project.manager_project import ManagerProject
from manager_venv.manager_venv import ManagerVenv


class ManagerFlask(ManagerProject):
    """Manages Flask projects by extending the ManagerProject class.

    This class handles the creation of a Flask project, including the required directories,
    the app.py file, and a basic index.html template.
    """

    def __init__(self, venv: ManagerVenv, project_name: str = "project_flask") -> None:
        """Initialize the ManagerFlask with a virtual environment and project name.

        Args:
            venv (ManagerVenv): The ManagerVenv instance managing the virtual environment.
            project_name (str): The name of the Flask project.
        """
        super().__init__(venv, project_name)

    def _create_project(self) -> bool:
        """Create a Flask project within the virtual environment.

        Installs Flask if it is not already installed, creates the necessary project
        directories, and generates a basic 'app.py' and 'index.html'.

        Returns:
            bool: True if the Flask project was created successfully, False otherwise.
        """
        output = True
        try:
            if not self._venv.check_library("flask"):
                print("Installing the flask...")
                print(self._venv.install_library("flask")[0][32:43])
            if not self._exists_dir():
                self._create_templates()
                self._create_app()
                self._create_index()
                print(f"Flask project '{self._name}' created successfully!")
                output = True
        except Exception as e:
            print(f"Error creating Flask project '{self._name}': {e}")
            output = False
        return output

    def _create_templates(self) -> None:
        self._create_directory("templates")

    def _create_app(self) -> None:
        app_py_content = """from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    """
        self._create_file("app.py", app_py_content)

    def _create_index(self):
        index_html_content = """<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home</title>
    </head>
        <body>
            <h1>Welcome to Flask!</h1>
        </body>
</html>
"""
        self._create_file("templates\\index.html", index_html_content)

    def runserver(self) -> list[type[str]]:
        operator = ";"
        if self._venv._platform == "Windows":
            operator = "&&"
        output: list[type[str]] = self._venv.run_venv_command(
            f"python {self._dir_path}\\app.py {operator} exit"
        )
        return output
