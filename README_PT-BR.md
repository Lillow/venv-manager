# venv-manager (Português)

**venv-manager** é uma ferramenta de linha de comando que simplifica o gerenciamento de ambientes virtuais Python, permitindo a criação de ambientes, a instalação de bibliotecas e a configuração de projetos Django e Flask. Ela automatiza grande parte da configuração inicial para novos projetos Python.

## 1. Estrutura do Projeto

### 1.1 Diretório `manager_venv/`

O diretório `manager_venv` contém funcionalidades para criação e gerenciamento de ambientes virtuais Python.

#### 1.1.1 Módulo `manager_venv.py`

O módulo `manager_venv.py` define a classe `ManagerVenv`, responsável por criar e gerenciar o ambiente virtual Python. Suas principais funcionalidades incluem:

- **Criação de Ambiente Virtual:** Cria um ambiente virtual com pip habilitado.
- **Execução de Comandos:** Permite executar comandos dentro do ambiente virtual.
- **Instalação de Bibliotecas:** Instala pacotes Python no ambiente virtual.
- **Verificação de Bibliotecas:** Verifica se uma biblioteca específica está instalada.
- **Listagem de Bibliotecas:** Lista todas as bibliotecas instaladas no ambiente virtual.

### 1.2 Diretório `manager_django/`

Contém o módulo `manager_django.py` com a classe `ManagerDjango`, responsável por criar e gerenciar projetos Django. As principais funcionalidades incluem:

- **Verificação e Instalação do Django:** Verifica se o Django está instalado no ambiente virtual e realiza a instalação, se necessário.
- **Criação de Projeto Django:** Cria um novo projeto Django com o nome especificado.

### 1.3 Diretório `manager_flask/`

Contém o módulo `manager_flask.py` com a classe `ManagerFlask`, responsável por criar e gerenciar projetos Flask. As principais funcionalidades incluem:

- **Verificação e Instalação do Flask:** Verifica se o Flask está instalado no ambiente virtual e realiza a instalação, se necessário.
- **Criação de Projeto Flask:** Cria um novo projeto Flask com o nome especificado.

## 2. Como Usar

1. **Baixe o Executável ou Rode o Script:**
   - Baixe o arquivo `venv_manager.exe` ou execute o script diretamente.

2. **Executar o Arquivo:**
   - Coloque o executável (ou script) no diretório onde deseja criar o projeto e execute-o.

3. **Criar ou Selecionar um Ambiente Virtual:**
   - Insira o nome do ambiente virtual para criá-lo ou encontrá-lo. Se nada for especificado, o nome padrão será "venv".

![image](https://github.com/user-attachments/assets/901ff244-bece-468a-a968-5b4f931f8f08)


4. **Menu de Opções do Ambiente Virtual:**
   - Escolha uma das opções para gerenciar seu ambiente virtual:
     - **1 - Manage project:** Gerenciar ou criar um projeto.
     - **2 - Install library:** Instalar bibliotecas Python.
     - **3 - List libraries:** Listar todas as bibliotecas instaladas.
     - **4 - Execute command:** Executar comandos personalizados dentro do ambiente virtual.
     - **0 - Leave:** Sair da ferramenta.

5. **Menu de Gerenciamento de Projeto:**
   - Selecione a opção "1 - Manage project" para criar ou gerenciar um projeto. Após inserir o nome do projeto, o seguinte menu será exibido:
     - **1 - Django:** Configura o projeto como um projeto Django.
     - **2 - Flask:** Configura o projeto como um projeto Flask.
     - **0 - Leave:** Retorna ao menu anterior.

6. **Menu de Opções do Projeto (Django ou Flask):**
   - Dependendo do tipo de projeto escolhido, as opções específicas aparecerão:
     - **1 - Run server:** Inicia o servidor do projeto.
     - **0 - Leave:** Retorna ao menu anterior.

## 3. Funcionalidades

1. **Gerenciar Ambiente Virtual:** Cria um novo ambiente virtual ou utiliza um existente.
2. **Gerenciar Projeto:** Permite criar e configurar um projeto Django ou Flask.
3. **Instalar Biblioteca:** Instala qualquer pacote Python no ambiente virtual.
4. **Listar Bibliotecas:** Lista todas as bibliotecas instaladas no ambiente virtual.
5. **Executar Comando:** Executa comandos personalizados dentro do ambiente virtual.
6. **Executar Servidor do Projeto:** Inicia o servidor de desenvolvimento.
7. **Sair:** Encerra a ferramenta.

## 4. Requisitos

- **Python:** Versão 3.12 ou superior.

##

 5. Contribuição

Contribuições são bem-vindas! Siga estas etapas para contribuir:

1. **Fork do repositório:** Crie um fork do repositório no GitHub.
2. **Clone o repositório:** Clone-o em seu ambiente local usando `git clone`.
3. *Crie um Branch:** Crie um novo branch para seu recurso ou correção de bug (`git checkout -b your-branch-name`).
4. **Faça as alterações:** implemente suas alterações e adicione testes.
5. **Execute os testes:** Certifique-se de que todos os testes sejam aprovados antes de enviar sua solicitação pull.
6. **Sincronize com o repositório original:** Sincronize seu branch com o repositório original para evitar conflitos.
7. **Envie a solicitação pull:** Envie sua solicitação pull para o repositório principal, descrevendo as alterações e sua finalidade.

### 5.1 Diretrizes de código e estilo

- **PEP 8:** Siga as diretrizes de estilo do PEP 8.
- **Documentação:** Adicione ou atualize a documentação para alterações significativas.
- **Comentários:** Use comentários claros e concisos para explicar seu código.

## 6. Licença

Este projeto está licenciado sob a Licença MIT.
