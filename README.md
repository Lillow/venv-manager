# Python Project Creator

python-project-creator é um projeto que automatiza a criação de ambientes virtuais Python e projetos Django, facilitando o setup inicial de novos projetos.




## 1. venv_creator/

O diretório venv_creator contém as funcionalidades para a criação e manipulação de ambientes virtuais.
### 1.1 venv_creator.py

Este módulo define a classe VenvCreator, que é responsável por criar e gerenciar um ambiente virtual Python. As funcionalidades principais incluem:

- **Criação do Ambiente Virtual**: Cria um ambiente virtual com pip habilitado.
- **Execução de Comandos no Ambiente Virtual**: Permite a execução de comandos dentro do ambiente virtual.
- **Instalação de Bibliotecas**: Instala bibliotecas Python dentro do ambiente virtual.
- **Verificação de Bibliotecas**: Verifica se uma biblioteca específica está instalada.
- **Listagem de Bibliotecas**: Lista as bibliotecas instaladas no ambiente virtual.
    
**Exemplo de Uso:**

```python

from venv_creator import VenvCreator

venv = VenvCreator(venv_name="my_env")
venv.install_library("requests")
venv.execute_venv_command("python --version")

```



## 2. django_creator.py

O módulo django_creator.py define a classe DjangoCreator, que é responsável por criar projetos Django dentro de um ambiente virtual.
Funcionalidades:

- **Verificação e Instalação do Django:** Verifica se o Django está instalado no ambiente virtual e, caso não esteja, realiza a instalação.
- **Criação de Projetos Django:** Cria um novo projeto Django com o nome especificado.

**Exemplo de Uso:**

```python

from venv_creator.venv_creator import VenvCreator
from django_creator import DjangoCreator

venv = VenvCreator(venv_name="my_env")
django_project = DjangoCreator(project_name="my_django_project", venv=venv)

```



## Como Usar

    Clone o Repositório:

    bash

    git clone <URL-do-repositório>
    cd python-project-creator

    Criação do Ambiente Virtual:

    Use a classe VenvCreator para criar e gerenciar um ambiente virtual.

    Criação de um Projeto Django:

    Use a classe DjangoCreator para criar um novo projeto Django dentro do ambiente virtual.

## Requisitos

    Python 3.x
    venv para a criação de ambientes virtuais

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.
