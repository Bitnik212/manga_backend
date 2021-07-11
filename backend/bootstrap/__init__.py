from bootstrap.MainApp import MainApp
from bootstrap.SubApp import SubApp
from bootstrap.API import APIApp as APIClass, APIVersion0
from bootstrap.account import AccountApp
from fastapi.middleware.gzip import GZipMiddleware
app_class = MainApp()
app = app_class.get_instance()
app_routes = app_class.routes
app_class.config = app_class.config

account = AccountApp()
account_i = account.get_instance()


account_i.include_router(
    account.routes.latest.SignIn,
)

# @account_i.get("/")
# def read_root():
#     return {"Bruh": f"Hello {account.config.mount_path+'/v'+str(account.now_version.version_code)}"}
#
#
# @apiV1_i.get("/")
# def read_root():
#     return {"Bruh": f"Hello {apiV1.config.mount_path+'fff/v'+str(apiV1.now_version.version_code+1)}"}


@app.get("/")
def read_root():
    return {"Bruh": f"Hello {app_class.config.mount_path+'/v'+str(app_class.now_version.version_code)}"}


app.mount(account.config.mount_path, account_i)
# app.mount(apiV1.config.mount_path, apiV1_i)
