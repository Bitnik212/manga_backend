from bootstrap import SubApp
from routes import AdminkaRoutes


class Adminka(SubApp):

    def __init__(self):
        super().__init__()
        self.subclass_name = "Adminka"
        self.version = AdminkaRoutes()