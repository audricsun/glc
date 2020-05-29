from __future__ import absolute_import
from __future__ import unicode_literals

from click.testing import CliRunner

from glc import __version__
from glc.cli.entry import cli


def test_cli_entry_version():
    """
    Command:
    glc --version
    Expect:
    return version from glc.__version__
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert f"version {__version__}" in result.output


def test_cli_entry_config_param_path_no_exist():
    """
    Command:
    glc --config SOME_FOLDER_NOT_EXIST
    Expect:
    Return code 2, folder not exist.
    """
    runner = CliRunner()
    folder = "SOME_FOLDER_NOT_EXIST"
    result = runner.invoke(cli, ["--config", folder])
    assert result.exit_code == 2
    assert f"Directory '{folder}' does not exist." in result.output


def test_cli_entry_config_param_with_no_sub_cmd():
    """
    Command:
    glc --config ./ https://gitlab.com
    Expect:
    Return code 2, missing command
    """
    runner = CliRunner()
    folder = "./"
    result = runner.invoke(cli, ["--config", folder])
    assert result.exit_code == 2
    assert "Missing command." in result.output


def test_cli_entry_sub_cmd_load(mocker):
    """
    Expect, load all sub commands,
    and shows on --help
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    for sub in ["repo", "user", "config", "info", "ns"]:
        assert sub in result.output


def test_cli_entry_global_config_default():
    runner = CliRunner()
    result = runner.invoke(cli, ["info"])
    assert result.exit_code == 0


def test_cli_entry_global_config_option_given():
    runner = CliRunner()
    result = runner.invoke(cli, ["--config", "./", "info"])
    assert result.exit_code == 0
