from manager_menu.manager_menu import ManagerMenu


class MenuInitial(ManagerMenu):
    def __init__(self, banner: str, msg_manager: str) -> None:
        super().__init__(banner)
        self.print_banner()
        self.manager_name: str = input(msg_manager)
