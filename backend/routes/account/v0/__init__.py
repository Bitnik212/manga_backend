from enum import Enum

from routes.account.v0.SignIn import router as SignIn


class AccountRoutesV0(Enum):
    SignIn = SignIn

    # def __init__(self):
    #     self.SignIn = SignIn

