import routes.api.v0.About
import routes.api.v0.Basics

class APIRoutesV0:

    def __init__(self):
        self.about = About.router
        self.basics = Basics.router

