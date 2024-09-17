from typing import Callable

try:
    import msvcrt
except ImportError:
    import sys
    import termios
    import tty

    try:
        msvcrt.getch()
    except ImportError:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


class Options:
    def __init__(
        self, options: dict[int, tuple[str, Callable]], exit_option: int = 0
    ) -> None:
        self._options = options
        self._exit_option = exit_option

    def show(self) -> None:
        # wait_for_keypress()
        for key, (description, _) in self._options.items():
            print(f"{key} - {description}")
        print(f"{self._exit_option} - Leave")

    def choice(self) -> None:
        while True:
            self.show()
            option = input("\nChoose an option: ")

            if option.isdigit() and int(option) in self._options:
                _, action = self._options[int(option)]
                action()
            elif option == str(self._exit_option):
                print("Leaving...")
                break
            else:
                print("Invalid option. Please try again.")
