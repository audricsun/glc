from click.testing import CliRunner
from gli.cli.subs.c_config import cli
from gli.cli.entry import GlobalConfig


def test_cli_sub_init_help_option():
    """
    Command:
    gli init --help
    Expect:
    Show help tips for arguments and options
    """
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'], obj=GlobalConfig(True))
    assert result.exit_code == 0


def test_cli_sub_init_init_from_scratch():
    pass


def test_cli_sub_init_init_from_scratch_default_config_path():
    """
    """
    pass


def test_cli_sub_init_wit_env_workspace():
    pass


def test_cli_sub_init_with_stored_workspace():
    pass


def test_cli_sub_init_with_config_path_given_as_args():
    pass


def test_cli_sub_init_with_config_path_given_as_envvar():
    pass
