from routes.SubAppRoutes import SubAppRoutes
from routes.account.v0 import AccountRoutesV0


class AccountRoutes(SubAppRoutes):

    def __init__(self):
        super().__init__()
        self.latest = AccountRoutesV0()
        self.v0 = AccountRoutesV0()
