from gli.config.conf import BaseConfigSection


def test_config_user_init():
    config = BaseConfigSection()
    assert config.info is None
