from bootstrap.API.version.Version0 import APIVersion0
from bootstrap.API.version.Version1 import APIVersion1
from bootstrap.SubAppVersion import SubAppVersion


class APIVersions:

    def __init__(self):
        self.versions: list[id(SubAppVersion)] = [APIVersion0, APIVersion1]

