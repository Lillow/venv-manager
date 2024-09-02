# Python Project Creator

**python-project-creator** é um projeto que automatiza a criação de ambientes virtuais Python, a instalação de bibliotecas, e a criação de projetos Django e Flask, facilitando o setup inicial de novos projetos.

## 1. Estrutura do Projeto

### 1.1 venv_creator/

O diretório `venv_creator` contém as funcionalidades para a criação e manipulação de ambientes virtuais.

#### 1.1.1 venv_creator.py

Este módulo define a classe `VenvCreator`, que é responsável por criar e gerenciar um ambiente virtual Python. As funcionalidades principais incluem:

- **Criação do Ambiente Virtual:** Cria um ambiente virtual com pip habilitado.
- **Execução de Comandos no Ambiente Virtual:** Permite a execução de comandos dentro do ambiente virtual.
- **Instalação de Bibliotecas:** Instala bibliotecas Python dentro do ambiente virtual.
- **Verificação de Bibliotecas:** Verifica se uma biblioteca específica está instalada.
- **Listagem de Bibliotecas:** Lista as bibliotecas instaladas no ambiente virtual.

### 1.2 project_creator/

O diretório `project_creator` contém as funcionalidades para a criação e manipulação de projetos.

#### 1.2.1 django_creator.py

Este módulo define a classe `DjangoCreator`, que é responsável por criar e gerenciar um projeto em Django. As funcionalidades principais incluem:

- **Verificação e Instalação do Django:** Verifica se o Django está instalado no ambiente virtual e, caso não esteja, realiza a instalação.
- **Criação de Projetos Django:** Cria um novo projeto Django com o nome especificado.

#### 1.2.2 flask_creator.py

Este módulo define a classe `FlaskCreator`, que é responsável por criar e gerenciar um projeto em Flask. As funcionalidades principais incluem:

- **Verificação e Instalação do Flask:** Verifica se o Flask está instalado no ambiente virtual e, caso não esteja, realiza a instalação.
- **Criação de Projetos Flask:** Cria um novo projeto Flask com o nome especificado.

## 2. Como Usar

1. **Baixar o Executável:** 
    - Baixe o arquivo `app.exe`.
    - ![Imagem ilustrativa de como baixar](path/to/image)

2. **Executar o Arquivo:**
    - Coloque o arquivo no diretório onde deseja criar o projeto e execute-o.
    - ![Imagem ilustrativa do `app.exe` em execução](path/to/image)

3. **Criar ou Selecionar um Ambiente Virtual:**
    - Digite o nome do ambiente virtual para criá-lo ou encontrá-lo, ou simplesmente pressione enter para usar o nome padrão "venv".
    - ![Imagem ilustrativa](path/to/image)

4. **Criar um Projeto Django ou Flask:**
    - Depois que o ambiente virtual for criado ou encontrado, escolha a opção desejada e pressione enter.
    - ![Imagem ilustrativa](path/to/image)

## 3. Requisitos

- **Python:** Versão 3.12 ou superior

## 4. Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## 5. Licença

Este projeto é licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

Danillo Silva `[@Lillow]`.
