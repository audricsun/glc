from __future__ import absolute_import
from __future__ import unicode_literals

import os

# from gli.utils.error import GitlabConfigNotExistError


class BaseConfigSection(object):
    def __init__(self, **kwargs):
        self.attr = kwargs

    @property
    def info(self):
        pass


class UserConfigSection(BaseConfigSection):
    """
    User config class
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class RemoteConfigSection(BaseConfigSection):
    """
    Remote config files
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class UserProfileSection(BaseConfigSection):
    """
    User profile class
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GitlabConfigFile(object):
    def __init__(self, config):
        self.config = config

    @property
    def exist(self):
        return os.path.exists(self.config)

    def init(self):
        pass
