from __future__ import absolute_import
from __future__ import unicode_literals


class GitlabAuthorisationError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class GitlabConfigNotExistError(Exception):
    pass
