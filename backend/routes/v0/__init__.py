import routes.v0.About
import routes.v0.Basics

class APIV0:

    def __init__(self):
        self.about = About.router
        self.basics = Basics.router