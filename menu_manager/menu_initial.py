from menu_manager.menu_manager import MenuManager
from utils.terminal_utils import clean_screen
import re


class MenuInitial(MenuManager):
    def __init__(self, banner: str, msg_manager: str) -> None:
        super().__init__(banner)
        self.print_banner()
        self.manager_name: str = (
            self._input_name(msg_manager) if msg_manager else msg_manager
        )

    def _input_name(self, msg_manager: str) -> str:
        while True:
            name: str = input(msg_manager)
            if self._check_name(name):
                return name

    def _check_name(self, name: str) -> bool:
        if name:
            name = name.lower()
            forbidden_names: set[str] = {"django", "flask", "admin", "config", "test"}
            if (
                len(name) < 4
                or not re.match(r"^[a-zA-Z0-9_-]+$", name)
                or name[0].isdigit()
                or name in forbidden_names
            ):
                return False
        return True
