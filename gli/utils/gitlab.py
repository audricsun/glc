from __future__ import absolute_import
from __future__ import unicode_literals

import json

import requests

# import asyncio


class wrapper_base(object):
    def __init__(self):
        super().__init__()
        self.attr = {}

    def __repr__(self):
        return {"name": self.attr, "age": 1}

    def get(self):
        pass

    def set(self):
        pass

    def diff(self):
        pass

    def flush(self):
        pass


class Gitlab(wrapper_base):
    def __init__(self, host, port=443, token=""):
        super().__init__()
        self.attr.update({"host": host, "port": port})

    def projects(self, **kwargs):
        host = self.attr.get("host")
        rsp = requests.get(
            f"{host}/api/v4/projects", headers={"PRIVATE-TOKEN": ""}, params=kwargs,
        )
        print(json.dumps(rsp.json(), indent=4))
        return [Project(**project) for project in rsp.json()]


class Namespace(wrapper_base):
    def __init__(self):
        super().__init__()


class Project(wrapper_base):
    def __init__(self, **kwargs):
        super().__init__()
        self.attr = kwargs

    def __repr__(self):
        return "Project: <{}>({})".format(self.attr["name"], self.attr["id"])


class Group(wrapper_base):
    def __init__(self):
        super().__init__()


class User(wrapper_base):
    def __init__(self):
        super().__init__()
