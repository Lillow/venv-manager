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

   ![image](https://github.com/user-attachments/assets/33031f06-ac2b-4b1b-879e-ae87a7f39b25)

   ![Screenshot 2024-10-25 at 10-18-59 venv-manager_venv_manager exe at main · Lillow_venv-manager](https://github.com/user-attachments/assets/8841c9e9-8aab-4bdd-bbda-82bf83140426)


2. **Executar o Arquivo:**
   - Coloque o executável (ou script) no diretório onde deseja criar o projeto e execute-o.

   ![image](https://github.com/user-attachments/assets/e4e19fde-1fdd-44cc-b8c9-27767107e23f)


3. **Criar ou Selecionar um Ambiente Virtual:**
   - Insira o nome do ambiente virtual para criá-lo ou encontrá-lo. Se nada for especificado, o nome padrão será "venv".

   ![image](https://github.com/user-attachments/assets/3b596f01-ef71-48b4-81b9-20b06f68b043)


4. **Menu de Opções do Ambiente Virtual:**
   - Escolha uma das opções para gerenciar seu ambiente virtual:
     - **1 - Manage project:** Gerenciar ou criar um projeto.
     - **2 - Install library:** Instalar bibliotecas Python.
     - **3 - List libraries:** Listar todas as bibliotecas instaladas.
     - **4 - Execute command:** Executar comandos personalizados dentro do ambiente virtual.
     - **0 - Leave:** Sair da ferramenta.
    
       ![image](https://github.com/user-attachments/assets/09fbfabb-2279-4495-b89f-a5ae5182c683)


5. **Criar ou Selecionar um Projeto:**
   - Insira o nome do projeto para criá-lo ou encontrá-lo.

   ![image](https://github.com/user-attachments/assets/30a744be-fbd8-44ea-95d4-5adcbaff5fd8)


6. **Menu de Gerenciamento de Projeto:**
   - Selecione a opção "1 - Manage project" para criar ou gerenciar um projeto. Após inserir o nome do projeto, o seguinte menu será exibido:
     - **1 - Django:** Configura o projeto como um projeto Django.
     - **2 - Flask:** Configura o projeto como um projeto Flask.
     - **0 - Leave:** Retorna ao menu anterior.
    
       ![image](https://github.com/user-attachments/assets/db5c3287-fc18-4683-bb0d-332cc7d11a91)


7. **Menu de Opções do Projeto (Django ou Flask):**
   - Dependendo do tipo de projeto escolhido, as opções específicas aparecerão:
     - **1 - Run server:** Inicia o servidor do projeto.
     - **0 - Leave:** Retorna ao menu anterior.
    
     ![image](https://github.com/user-attachments/assets/04e9e629-000f-4004-99be-b9b1d19c6404)
     ![image](https://github.com/user-attachments/assets/0d16edd2-fbf5-4757-b130-6114ba7c5e46)


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

## 5. Contribuição

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
