# venv-manager

[Read in English](./README.md)

**venv-manager** é uma ferramenta que simplifica o gerenciamento de ambientes virtuais Python, permitindo a criação de ambientes, instalação de bibliotecas e criação de projetos Django e Flask. Ele automatiza grande parte do setup inicial de novos projetos Python.

## 1. Estrutura do Projeto

### 1.1 venv_manager/

O diretório `venv_manager` contém as funcionalidades para criação e gerenciamento de ambientes virtuais.

#### 1.1.1 venv_manager.py

Este módulo define a classe `VenvManager`, responsável por criar e gerenciar um ambiente virtual Python. As principais funcionalidades incluem:

- **Criação do Ambiente Virtual:** Cria um ambiente virtual com pip habilitado.
- **Execução de Comandos no Ambiente Virtual:** Permite a execução de comandos dentro do ambiente virtual.
- **Instalação de Bibliotecas:** Instala bibliotecas Python no ambiente virtual.
- **Verificação de Bibliotecas:** Verifica se uma biblioteca específica está instalada.
- **Listagem de Bibliotecas:** Lista as bibliotecas instaladas no ambiente virtual.

### 1.2 project_manager/

O diretório `project_manager` contém as funcionalidades para a criação e gerenciamento de projetos Django e Flask.

#### 1.2.1 django_manager.py

Este módulo define a classe `DjangoManager`, responsável por criar e gerenciar projetos Django. As principais funcionalidades incluem:

- **Verificação e Instalação do Django:** Verifica se o Django está instalado no ambiente virtual e instala caso necessário.
- **Criação de Projetos Django:** Cria um novo projeto Django com o nome especificado.

#### 1.2.2 flask_manager.py

Este módulo define a classe `FlaskManager`, responsável por criar e gerenciar projetos Flask. As principais funcionalidades incluem:

- **Verificação e Instalação do Flask:** Verifica se o Flask está instalado no ambiente virtual e instala caso necessário.
- **Criação de Projetos Flask:** Cria um novo projeto Flask com o nome especificado.

## 2. Como Usar

1. **Baixar o Executável:**
    - Baixe o arquivo `app.exe`.

2. **Executar o Arquivo:**
    - Coloque o arquivo no diretório onde deseja criar o projeto e execute-o.

3. **Criar ou Selecionar um Ambiente Virtual:**
    - Digite o nome do ambiente virtual para criá-lo ou encontrá-lo, ou simplesmente pressione enter para usar o nome padrão "venv".

4. **Criar um Projeto Django ou Flask:**
    - Após o ambiente virtual ser criado ou encontrado, escolha a opção desejada e pressione enter.

## 3. Funcionalidades

1. **Criar projeto:** Instala o Django ou Flask e cria um projeto recebendo o nome do projeto.
2. **Instalar biblioteca:** Instala qualquer package Python no ambiente virtual.
3. **Listar bibliotecas:** Lista todas as bibliotecas instaladas no ambiente virtual.
4. **Executar comando:** Executa comandos dentro do ambiente virtual.
<!-- 5. **Criar executável:** Instala o `pyinstaller` (se necessário) e cria um executável do arquivo especificado. -->
5. **Sair:** Encerra a ferramenta.

## 4. Requisitos

- **Python:** Versão 3.12 ou superior

## 5. Contribuição

Contribuições são bem-vindas! Para contribuir, siga os passos abaixo:

1. **Fork o Repositório:** Crie um fork do repositório no GitHub.
2. **Clone o Repositório:** Clone-o para o seu ambiente local usando o comando `git clone`.
3. **Crie uma Branch:** Crie uma nova branch para sua feature ou correção (`git checkout -b nome-da-sua-branch`).
4. **Faça as Modificações:** Implemente suas mudanças e adicione testes.
5. **Execute os Testes:** Certifique-se de que todos os testes passem antes de enviar o pull request.
6. **Sincronize com o Repositório Original:** Sincronize sua branch com o repositório original para evitar conflitos.
7. **Envie o Pull Request:** Envie um pull request para o repositório principal, descrevendo as mudanças e o propósito delas.

### 5.1 Linhas de Código e Estilo

- **PEP 8:** Certifique-se de que seu código segue as diretrizes da PEP 8.
- **Documentação:** Adicione ou atualize a documentação para mudanças relevantes.
- **Comentários:** Use comentários claros e concisos para explicar o código.

## 6. Licença

Este projeto é licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
