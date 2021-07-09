from bootstrap.MainApp import MainApp
from bootstrap.SubApp import SubApp
from bootstrap.API import APIApp as APIClass, APIVersion0

app_class = MainApp()
app = app_class.get_instance()
app_routes = app_class.routes
app_class.config = app_class.config

api = APIClass()
apiV1 = APIClass()
apiV1.select_now_version(versionn=APIVersion0)
apiV1_i = apiV1.get_instance()
api_i = api.get_instance()


api_i.include_router(
    api.routes.latest.basics,
)
api_i.include_router(
    api.routes.latest.about,
)


@api_i.get("/")
def read_root():
    return {"Bruh": f"Hello {api.config.mount_path+'/v'+str(api.now_version.version_code)}"}
@apiV1_i.get("/")
def read_root():
    return {"Bruh": f"Hello {apiV1.config.mount_path+'fff/v'+str(apiV1.now_version.version_code+1)}"}


@app.get("/")
def read_root():
    return {"Bruh": f"Hello {app_class.config.mount_path+'/v'+str(app_class.now_version.version_code)}"}


app.mount(api.config.mount_path, api_i)
app.mount(apiV1.config.mount_path, apiV1_i)
