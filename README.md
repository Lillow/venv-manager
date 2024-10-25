# venv-manager

[Leia em Português](./README_PT-BR.md)

**venv-manager** is a command-line tool that simplifies Python virtual environment management, enabling the creation of virtual environments, library installations, and setup for Django and Flask projects. It automates much of the initial setup needed for new Python projects.

## 1. Project Structure

### 1.1 manager_venv/

The `manager_venv` directory contains functionalities for creating and managing Python virtual environments.

#### 1.1.1 manager_venv.py

This module defines the `ManagerVenv` class, responsible for creating and managing Python virtual environments. Key functionalities include:

- **Virtual Environment Creation:** Creates a virtual environment with pip enabled.
- **Command Execution in Virtual Environment:** Allows commands to be executed within the virtual environment.
- **Library Installation:** Installs Python libraries within the virtual environment.
- **Library Verification:** Checks if a specific library is installed.
- **Library Listing:** Lists all installed libraries in the virtual environment.

### 1.2 manager_django/

Contains `manager_django.py` with the `ManagerDjango` class, responsible for creating and managing Django projects. Key functionalities include:

- **Django Verification and Installation:** Checks if Django is installed in the virtual environment and installs it if necessary.
- **Django Project Creation:** Creates a new Django project with the specified name.

### 1.3 manager_flask/

Contains `manager_flask.py` with the `ManagerFlask` class, responsible for creating and managing Flask projects. Key functionalities include:

- **Flask Verification and Installation:** Checks if Flask is installed in the virtual environment and installs it if necessary.
- **Flask Project Creation:** Creates a new Flask project with the specified name.

## 2. How to Use

1. **Download the Executable or Run the Script:**
   - Download the `venv_manager.exe` file or run the Python script directly.

2. **Execute the File:**
   - Place the executable (or script) in the directory where you want to create the project and execute it.

3. **Create or Select a Virtual Environment:**
   - Enter the name of the virtual environment to create or locate it. If no name is provided, the default name is "venv".

4. **Virtual Environment Options Menu:**
   - Once in the environment, you’ll see the following menu options:
     - **1 - Manage project:** Enter the project management menu.
     - **2 - Install library:** Install libraries in the environment.
     - **3 - List libraries:** List installed libraries.
     - **4 - Execute command:** Execute custom commands within the environment.
     - **0 - Leave:** Exit the tool.

5. **Project Management Menu:**
   - Selecting "1 - Manage project" will prompt for the project name. If the project doesn’t exist, it will be created. You’ll then see:
     - **1 - Django:** Sets up a Django project.
     - **2 - Flask:** Sets up a Flask project.
     - **0 - Leave:** Return to the previous menu.

6. **Project Options Menu (Django or Flask):**
   - If a Django or Flask project is selected, the respective menu will appear with options:
     - **1 - Run server:** Starts the project’s development server.
     - **0 - Leave:** Return to the previous menu.

## 3. Functionalities

1. **Manage Virtual Environment:** Creates or reuses a virtual environment.
2. **Manage Project:** Sets up a Django or Flask project if it does not already exist.
3. **Install Library:** Installs any specified Python package.
4. **List Libraries:** Shows all libraries installed in the virtual environment.
5. **Execute Command:** Allows custom commands to be run within the environment.
6. **Run Project Server:** Starts the Django or Flask server for development.
7. **Exit:** Closes the application.

## 4. Requirements

- **Python:** Version 3.12 or higher.

## 5. Contribution

Contributions are welcome! Follow these steps to contribute:

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