# Python Project Creator

**python-project-creator** é um projeto que automatiza a criação de ambientes virtuais Python, a instalação de bibliotecas, e a criação de projetos Django e Flask, facilitando o setup inicial de novos projetos.

**python-project-creator** is a project that automates the creation of Python virtual environments, the installation of libraries, and the creation of Django and Flask projects, simplifying the initial setup of new projects.

## 1. Estrutura do Projeto | Project Structure

### 1.1 venv_creator/

O diretório `venv_creator` contém as funcionalidades para a criação e manipulação de ambientes virtuais.

The `venv_creator` directory contains functionalities for creating and managing virtual environments.

#### 1.1.1 venv_creator.py

Este módulo define a classe `VenvCreator`, que é responsável por criar e gerenciar um ambiente virtual Python. As funcionalidades principais incluem:

This module defines the `VenvCreator` class, which is responsible for creating and managing a Python virtual environment. The main functionalities include:

- **Criação do Ambiente Virtual:** Cria um ambiente virtual com pip habilitado.
  
  **Virtual Environment Creation:** Creates a virtual environment with pip enabled.
  
- **Execução de Comandos no Ambiente Virtual:** Permite a execução de comandos dentro do ambiente virtual.
  
  **Command Execution in Virtual Environment:** Allows the execution of commands within the virtual environment.
  
- **Instalação de Bibliotecas:** Instala bibliotecas Python dentro do ambiente virtual.
  
  **Library Installation:** Installs Python libraries within the virtual environment.
  
- **Verificação de Bibliotecas:** Verifica se uma biblioteca específica está instalada.
  
  **Library Verification:** Checks if a specific library is installed.
  
- **Listagem de Bibliotecas:** Lista as bibliotecas instaladas no ambiente virtual.
  
  **Library Listing:** Lists the libraries installed in the virtual environment.

### 1.2 project_creator/

O diretório `project_creator` contém as funcionalidades para a criação e manipulação de projetos.

The `project_creator` directory contains functionalities for creating and managing projects.

#### 1.2.1 django_creator.py

Este módulo define a classe `DjangoCreator`, que é responsável por criar e gerenciar um projeto em Django. As funcionalidades principais incluem:

This module defines the `DjangoCreator` class, which is responsible for creating and managing a Django project. The main functionalities include:

- **Verificação e Instalação do Django:** Verifica se o Django está instalado no ambiente virtual e, caso não esteja, realiza a instalação.
  
  **Django Verification and Installation:** Verifies if Django is installed in the virtual environment and installs it if necessary.
  
- **Criação de Projetos Django:** Cria um novo projeto Django com o nome especificado.
  
  **Django Project Creation:** Creates a new Django project with the specified name.

#### 1.2.2 flask_creator.py

Este módulo define a classe `FlaskCreator`, que é responsável por criar e gerenciar um projeto em Flask. As funcionalidades principais incluem:

This module defines the `FlaskCreator` class, which is responsible for creating and managing a Flask project. The main functionalities include:

- **Verificação e Instalação do Flask:** Verifica se o Flask está instalado no ambiente virtual e, caso não esteja, realiza a instalação.
  
  **Flask Verification and Installation:** Verifies if Flask is installed in the virtual environment and installs it if necessary.
  
- **Criação de Projetos Flask:** Cria um novo projeto Flask com o nome especificado.
  
  **Flask Project Creation:** Creates a new Flask project with the specified name.

## 2. Como Usar | How to Use

1. **Baixar o Executável:**
   **Download the Executable:**
    - Baixe o arquivo `app.exe`.
    - Download the `app.exe` file.
    - ![app-img](https://github.com/user-attachments/assets/aa10e5d1-6a8f-4edd-8b7c-a74b9f818d29)
    - ![download-img](https://github.com/user-attachments/assets/ba067cc6-103f-4443-b552-ec6064c86d29)

3. **Executar o Arquivo:**
   **Run the File:**
    - Coloque o arquivo no diretório onde deseja criar o projeto e execute-o.
    - Place the file in the directory where you want to create the project and execute it.
    - ![app-img2](https://github.com/user-attachments/assets/514faf76-db9a-4065-b781-241aad96fb93)
  
   

5. **Criar ou Selecionar um Ambiente Virtual:**
   **Create or Select a Virtual Environment:**
    - Digite o nome do ambiente virtual para criá-lo ou encontrá-lo, ou simplesmente pressione enter para usar o nome padrão "venv".
    - Enter the name of the virtual environment to create or find it, or simply press enter to use the default name "venv."
    - ![project-creator-img](https://github.com/user-attachments/assets/fdf79851-941c-456d-918b-32295fd586b3)
  
   

7. **Criar um Projeto Django ou Flask:**
   **Create a Django or Flask Project:**
    - Depois que o ambiente virtual for criado ou encontrado, escolha a opção desejada e pressione enter.
    - After the virtual environment is created or found, choose the desired option and press enter.
    - ![project-creator-img2](https://github.com/user-attachments/assets/e31af3e8-5ef5-42d4-b9ba-18f731a726f5)
  

   
## 3. Requisitos | Requirements

- **Python:** Versão 3.12 ou superior
  
  **Python:** Version 3.12 or higher

## 4. Contribuição | Contribution

Contribuições são bem-vindas! Para contribuir, siga os passos abaixo:

Contributions are welcome! To contribute, follow the steps below:

1. **Fork o Repositório:** Crie um fork do repositório no GitHub para sua conta.
   
   **Fork the Repository:** Create a fork of the repository on GitHub to your account.
  
2. **Clone o Repositório:** Clone o repositório para o seu ambiente local usando o comando `git clone`.
   
   **Clone the Repository:** Clone the repository to your local environment using the `git clone` command.
  
3. **Crie uma Branch:** Crie uma nova branch para desenvolver sua feature ou corrigir um bug (`git checkout -b nome-da-sua-branch`).
   
   **Create a Branch:** Create a new branch to develop your feature or fix a bug (`git checkout -b your-branch-name`).
  
4. **Faça as Modificações:** Implemente suas mudanças e adicione testes para garantir que tudo funcione corretamente.
   
   **Make the Changes:** Implement your changes and add tests to ensure everything works correctly.
  
5. **Execute os Testes:** Certifique-se de que todos os testes passem antes de enviar seu PR. Se necessário, adicione novos testes para cobrir as mudanças.
   
   **Run the Tests:** Make sure all tests pass before submitting your PR. If necessary, add new tests to cover the changes.
  
6. **Commit as Mudanças:** Faça commit das suas mudanças (`git commit -m "Descrição das mudanças"`).
   
   **Commit the Changes:** Commit your changes (`git commit -m "Description of changes"`).
  
7. **Sincronize com o Repositório Original:** Antes de criar um pull request, sincronize sua branch com o repositório original para evitar conflitos (`git pull origin main`).
   
   **Sync with the Original Repository:** Before creating a pull request, sync your branch with the original repository to avoid conflicts (`git pull origin main`).
  
8. **Envie o Pull Request:** Envie um pull request para o repositório principal descrevendo as mudanças e o propósito delas.
   
   **Submit the Pull Request:** Submit a pull request to the main repository, describing the changes and their purpose.

### 4.1 Linhas de Código e Estilo | Code and Style Guidelines

- **PEP 8:** Certifique-se de que seu código segue as diretrizes de estilo da PEP 8.
  
  **PEP 8:** Ensure your code follows PEP 8 style guidelines.
  
- **Documentação:** Adicione ou atualize a documentação sempre que fizer alterações relevantes no código.
  
  **Documentation:** Add or update documentation whenever you make significant changes to the code.
  
- **Comentários:** Use comentários claros e concisos para explicar a lógica do código.
  
  **Comments:** Use clear and concise comments to explain the logic of the code.

## 5. Licença | License

Este projeto é licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

This project is licensed under the MIT license. See the `LICENSE` file for more details.
