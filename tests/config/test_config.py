from __future__ import absolute_import
from __future__ import unicode_literals

from glc.config.conf import BaseConfigSection


def test_config_user_init():
    config = BaseConfigSection()
    assert config.info is None
