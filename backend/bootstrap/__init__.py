from fastapi.responses import RedirectResponse

from bootstrap.MainApp import MainApp
from bootstrap.SubApp import SubApp
from bootstrap.API import APIApp as APIClass, APIVersion0
from bootstrap.account import AccountApp

app_class = MainApp()
app = app_class.get_instance()

account = AccountApp()
account_i = account.get_instance()


@app.get("/")
def redirect_to_docs():
    return RedirectResponse("docs")


app.mount(account.config.mount_path, account_i)
