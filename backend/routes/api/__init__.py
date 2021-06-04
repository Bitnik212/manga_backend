from routes.SubAppRoutes import SubAppRoutes
from routes.api.v0 import APIRoutesV0

class APIRoutes(SubAppRoutes):

    def __init__(self):
        super().__init__()
        self.v0 = APIRoutesV0()
        self.latest = APIRoutesV0()
