from project_creator.project_creator import ProjectCreator


class FlaskCreator(ProjectCreator):
    def _create_project(self) -> bool:
        try:
            if not self._venv.check_library("flask"):
                self._venv.install_library("flask")

            directories = [
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

            print(f"Flask project '{self._project_name}' created successfully!")
            return True
        except Exception as e:
            print(f"Error creating Flask project '{self._project_name}': {e}")
            return False
