import os
import pytest
from venv_creator import VenvCreator


# Testa se o ambiente foi criado corretamente
@pytest.mark.parametrize(('venv_creator'), [(VenvCreator())])
def test_venv_creation(venv_creator):
    assert venv_creator.is_created, "Ambiente virtual não foi criado com sucesso"
    assert os.path.exists(
        venv_creator._venv_name), "O diretório do ambiente virtual não existe"


# Testa se uma biblioteca pode ser instalada no ambiente virtual
@pytest.mark.parametrize(('venv_creator', 'library_name'), [(VenvCreator(), 'requests')])
def test_install_library(venv_creator, library_name):
    assert venv_creator.install_library(
        library_name), "Falha ao instalar a biblioteca 'requests'"

# Testa se a listagem de bibliotecas funciona corretamente
@pytest.mark.parametrize(('venv_creator'), [(VenvCreator())])
def test_list_library(venv_creator):
    assert venv_creator.list_library(), "Falha ao listar as bibliotecas instaladas"

# Testa a execução de um comando customizado dentro do ambiente virtual
@pytest.mark.parametrize(('venv_creator'), [(VenvCreator())])
def test_execute_venv_command(venv_creator):
    command = "python --version"
    assert venv_creator.execute_venv_command(
        command), f"Falha ao executar o comando: {command}"
