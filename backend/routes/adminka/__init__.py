from routes.SubAppRoutes import SubAppRoutes


class AdminkaRoutes(SubAppRoutes):

    def __init__(self):
        super().__init__()
        self.api_name = "adminka"
        self.v0 = None
        self.latest = self.v0
        self.version_code = 0