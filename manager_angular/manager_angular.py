from manager.manager import Manager


class ManagerAngular(Manager):
    def __init__(self, name: str = "project_angular") -> None:
        super().__init__(name)

    def _create(self):
        pass
