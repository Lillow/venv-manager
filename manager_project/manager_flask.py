from manager_project.manager_project import ManagerProject
from manager_venv.manager_venv import ManagerVenv


class ManagerFlask(ManagerProject):
    """Manages Flask projects by extending the ManagerProject class.

    This class handles the creation of a Flask project, including the required directories,
    the app.py file, and a basic index.html template.
    """

    def __init__(self, venv: ManagerVenv, project_name: str) -> None:
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
                directories: list[str] = [
                    "templates",
                    "static",
                    "static/css",
                    "static/js",
                    "static/images",
                ]
                self._create_directories(directories)

                app_py_content = """from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    """
                self._create_file(f"{self._name}//app.py", app_py_content)

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
                self._create_file(
                    f"{self._name}//templates/index.html", index_html_content
                )

                print(f"Flask project '{self.__str__()}' created successfully!")
                output = True
        except Exception as e:
            print(f"Error creating Flask project '{self.__str__()}': {e}")
            output = False
        return output
