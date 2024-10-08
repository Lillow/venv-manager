from typing import Callable
from utils.terminal_utils import clean_screen


class Options:
    def __init__(
        self,
        options: dict[int, tuple[str, Callable]],
        banner: str = None,
        exit_option: int = 0,
    ) -> None:
        self._options = options
        self._exit_option: int = exit_option
        self._banner: str = banner

    def show(self) -> None:
        if self._banner:
            print(self._banner,"\n")
        for key, (description, _) in self._options.items():
            print(f"{key} - {description}")
        print(f"{self._exit_option} - Leave")

    def choice(self) -> None:
        """Captura a escolha do usuário e executa a ação correspondente"""
        while True:
            self.show()
            option = input("\nChoose an option: ")

            match option:
                case str() if option.isdigit() and int(option) in self._options:
                    _, action = self._options[int(option)]
                    action()  # Executa a ação associada à opção
                case str() if option == str(self._exit_option):
                    print("Leaving...")
                    clean_screen()  # Limpa a tela antes de sair
                    break
                case _:
                    clean_screen()
                    print("Invalid option. Please try again.\n")
