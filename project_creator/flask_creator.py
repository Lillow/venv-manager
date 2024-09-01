from project_creator.project_creator import ProjectCreator


class FlaskCreator(ProjectCreator):

    def _create_project(self) -> bool:
        checker = False
        try:
            dirs = [
                'templates',
                'static',
                'static/css',
                'static/js',
                'static/images',
            ]
            self._directory_creator(dirs)

            app_py_content = """from flask import Flask, render_template

    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    if __name__ == '__main__':
        app.run(debug=True)
    """
            self._file_creator("app.py", app_py_content)

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
            self._file_creator("templates/index.html", app_py_content)

            requirements_content = "Flask"
            self._file_creator("requirements.txt", app_py_content)

            print(f"Projeto {self._project_name} criado com sucesso!")
            checker = True
        except Exception as e:
            print(f"Erro ao criar o projeto flask {self._project_name}: {e}")

        return checker
