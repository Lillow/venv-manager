from manager_project.manager_project import ManagerProject
from manager_venv.manager_venv import ManagerVenv


class ManagerFlask(ManagerProject):
    def __init__(self, venv: ManagerVenv, project_name: str) -> None:
        super().__init__(venv, project_name)

    def _create_project(self) -> bool:
        output = True
        try:
            if not self._venv.check_library("flask"):
                self._venv.install_library("flask")
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
                self._create_file("app.py", app_py_content)

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
                self._create_file("templates/index.html", index_html_content)

                print(f"Flask project '{self.__str__()}' created successfully!")
                output = True
        except Exception as e:
            print(f"Error creating Flask project '{self.__str__()}': {e}")
            output = False
        return output
