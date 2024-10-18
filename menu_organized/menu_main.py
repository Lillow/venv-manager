from menu_organized.menu_initial import MenuInitial
from menu_organized.menu_options import MenuOptions
from utils.terminal_utils import pause_and_clear, clean_screen, print_line


class MenuMain:
    def __init__(
        self, menu_initial: MenuInitial, manager: any, menu_options: MenuOptions
    ) -> None:
        self._menu_initial: MenuInitial = menu_initial
        self._manager = manager
        self._menu_options = menu_options
