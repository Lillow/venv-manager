# from venv_creator.venv_creator import VenvCreator


# def create_executable(script_name, venv: VenvCreator):
#     try:
#         if not venv.check_library("PyInstaller"):
#             venv.install_library("PyInstaller")
#     except e:
        

#     command = [sys.executable, "-m", "PyInstaller", "--onefile", script_name]

#     # Adiciona o ícone se fornecido
#     if icon_path:
#         command.extend(["--icon", icon_path])

#     # Executa o comando
#     try:
#         subprocess.run(command, check=True)
#         print(f"Executável criado com sucesso! Você pode encontrá-lo na pasta 'dist'.")
#     except subprocess.CalledProcessError as e:
#         print(f"Ocorreu um erro ao tentar criar o executável: {e}")
#     except Exception as e:
#         print(f"Erro inesperado: {e}")


# if __name__ == "__main__":
#     script = "app.py"  # Nome do script que você deseja transformar em executável
#     icon = "C:/Users/danil/workspace/PythonProjects/venv-manager/exe.ico"

#     create_executable(script, icon)
