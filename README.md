# venv-manager

[Leia em Português](./README_PT-BR.md)

**venv-manager** is a tool that simplifies Python virtual environment management, allowing the creation of environments, the installation of libraries, and the setup of Django and Flask projects. It automates much of the initial setup needed for new Python projects.

## 1. Project Structure

### 1.1 venv_manager/

The `venv_manager` directory contains functionalities for creating and managing virtual environments.

#### 1.1.1 venv_manager.py

This module defines the `VenvManager` class, responsible for creating and managing a Python virtual environment. Key functionalities include:

- **Virtual Environment Creation:** Creates a virtual environment with pip enabled.
- **Command Execution in Virtual Environment:** Allows the execution of commands within the virtual environment.
- **Library Installation:** Installs Python libraries within the virtual environment.
- **Library Verification:** Checks if a specific library is installed.
- **Library Listing:** Lists the libraries installed in the virtual environment.

### 1.2 project_manager/

The `project_manager` directory contains functionalities for creating and managing Django and Flask projects.

#### 1.2.1 django_manager.py

This module defines the `DjangoManager` class, responsible for creating and managing Django projects. Key functionalities include:

- **Django Verification and Installation:** Verifies if Django is installed in the virtual environment and installs it if necessary.
- **Django Project Creation:** Creates a new Django project with the specified name.

#### 1.2.2 flask_manager.py

This module defines the `FlaskManager` class, responsible for creating and managing Flask projects. Key functionalities include:

- **Flask Verification and Installation:** Verifies if Flask is installed in the virtual environment and installs it if necessary.
- **Flask Project Creation:** Creates a new Flask project with the specified name.

## 2. How to Use

1. **Download the Executable:**
    - Download the `app.exe` file.

2. **Run the File:**
    - Place the file in the directory where you want to create the project and execute it.

3. **Create or Select a Virtual Environment:**
    - Enter the name of the virtual environment to create or find it, or simply press enter to use the default name "venv."

4. **Create a Django or Flask Project:**
    - After the virtual environment is created or found, choose the desired option and press enter.

## 3. Functionalities

1. **Create project:** Installs Django or Flask and creates a project by receiving the project name.
2. **Install library:** Installs any Python package in the virtual environment by receiving the package name.
3. **List libraries:** Lists all installed packages in the virtual environment.
4. **Execute command:** Executes commands within the virtual environment.
5. <!-- **Create executable:** Installs `pyinstaller` (if not already installed) and creates an executable from the specified file. -->
7. **Exit:** Leaves the tool.

## 4. Requirements

- **Python:** Version 3.12 or higher

## 5. Contribution

Contributions are welcome! Follow the steps below to contribute:

1. **Fork the Repository:** Create a fork of the repository on GitHub.
2. **Clone the Repository:** Clone it to your local environment using `git clone`.
3. **Create a Branch:** Create a new branch for your feature or bugfix (`git checkout -b your-branch-name`).
4. **Make the Changes:** Implement your changes and add tests.
5. **Run the Tests:** Ensure all tests pass before submitting your pull request.
6. **Sync with the Original Repository:** Sync your branch with the original repository to avoid conflicts.
7. **Submit the Pull Request:** Submit your pull request to the main repository, describing the changes and their purpose.

### 5.1 Code and Style Guidelines

- **PEP 8:** Follow PEP 8 style guidelines.
- **Documentation:** Add or update documentation for significant changes.
- **Comments:** Use clear and concise comments to explain your code.

## 6. License

This project is licensed under the MIT License. See the `LICENSE` file for details.
