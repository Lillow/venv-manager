from typing import Callable
from utils.terminal_utils import clean_screen
from manager_menu.manager_menu import ManagerMenu


class MenuOptions(ManagerMenu):
    """A class to display a menu of options, handle user input, and execute the corresponding actions.

    Attributes:
        options (dict[int, tuple[str, Callable]]): A dictionary where each key is an integer representing
            an option, and the value is a tuple with the option's description and the corresponding action (a callable).
        banner (str): An optional banner to be displayed above the menu.
        exit_option (int): The key for the exit option, which terminates the menu loop.
    """

    def __init__(
        self,
        banner: str,
        options: dict[int, tuple[str, Callable]],
        exit_option: int = 0,
    ) -> None:
        """Initialize the Options menu with a dictionary of options, an optional banner, and an exit option.

        Args:
            options (dict[int, tuple[str, Callable]]): Menu options with descriptions and corresponding actions.
            banner (str, optional): A string banner to display at the top of the menu. Defaults to None.
            exit_option (int, optional): The option number that triggers exiting the menu. Defaults to 0.
        """
        super().__init__(banner)
        self._options = options
        self._exit_option: int = exit_option

    def show(self) -> None:
        """Display the banner (if present) and the menu options to the user."""
        for key, (description, _) in self._options.items():
            print(f"{key} - {description}")
        print(f"{self._exit_option} - Leave")

    def choice(self) -> None:
        """Capture the user's input and execute the corresponding action.

        The method keeps running until the user selects the exit option.
        It clears the screen after each invalid input or when the user exits.
        """
        while True:
            self.show()
            option = input("\nChoose an option: ")

            match option:
                case str() if option.isdigit() and int(option) in self._options:
                    _, action = self._options[int(option)]
                    action()  # Execute the action associated with the chosen option
                case str() if option == str(self._exit_option):
                    print("Leaving...")
                    clean_screen()  # Clear the screen before exiting
                    break
                case _:
                    clean_screen()
                    print("Invalid option. Please try again.\n")
