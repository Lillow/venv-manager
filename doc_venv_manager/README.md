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

   ![image](https://github.com/user-attachments/assets/9efeb5b2-e2d2-48ca-bd72-c51e01b3dfc0)

   ![Screenshot 2024-10-25 at 10-18-59 venv-manager_venv_manager exe at main · Lillow_venv-manager](https://github.com/user-attachments/assets/f2bbb4aa-81f9-4738-b071-82fb48942ff8)



2. **Execute the File:**
   - Place the executable (or script) in the directory where you want to create the project and execute it.
  
     ![image](https://github.com/user-attachments/assets/e5c3656c-802a-44b8-87fa-35d23bdb0722)


3. **Create or Select a Virtual Environment:**
   - Enter the name of the virtual environment to create or locate it. If no name is provided, the default name is "venv".

   ![image](https://github.com/user-attachments/assets/20689a39-fe9b-49dc-ae24-8ee5a864c405)


4. **Virtual Environment Options Menu:**
   - Once in the environment, you’ll see the following menu options:
     - **1 - Manage project:** Enter the project management menu.
     - **2 - Install library:** Install libraries in the environment.
     - **3 - List libraries:** List installed libraries.
     - **4 - Execute command:** Execute custom commands within the environment.
     - **0 - Leave:** Exit the tool.
    
       ![image](https://github.com/user-attachments/assets/be7a45a5-8932-4ad3-805a-b99adc70685c)


5. **Create or select a project:**
   - Enter the name of the project environment to create or locate it.

   ![image](https://github.com/user-attachments/assets/b474c26f-9278-40ea-a528-b329d901448a)


6. **Project Management Menu:**
   - Selecting "1 - Manage project" will prompt for the project name. If the project doesn’t exist, it will be created. You’ll then see:
     - **1 - Django:** Sets up a Django project.
     - **2 - Flask:** Sets up a Flask project.
     - **0 - Leave:** Return to the previous menu.

     ![image](https://github.com/user-attachments/assets/7ad2a8fa-931f-44d1-aafa-5835e2698084)


7. **Project Options Menu (Django):**
   - Django options menu:
     - **1 - Run server:** Starts the project’s development server.
     - **2 - Start app** Create a django app.
     - **0 - Leave:** Return to the previous menu.
    
     ![Imagem do WhatsApp de 2024-11-02 à(s) 20 29 38_8aa8dc49](https://github.com/user-attachments/assets/c6f1a1bf-acd5-4e0a-a38a-bfe1ed3eb63f)
     

8. **Project Options Menu (Flask):**
   - Flask options menu:
     - **1 - Run server:** Starts the project’s development server.
     - **0 - Leave:** Return to the previous menu.
    
     ![image](https://github.com/user-attachments/assets/0d16edd2-fbf5-4757-b130-6114ba7c5e46)


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
