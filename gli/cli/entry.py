from __future__ import absolute_import
from __future__ import unicode_literals

import os
from os.path import expanduser

import click

from gli import __version__


class GlobalConfig:
    def __init__(self, verbose=False, profile=None, config=None):
        self.verbose = verbose
        self.profile = profile
        self.config = os.path.join(expanduser("~"), ".gli")
        if config is not None:
            self.config = config


pass_config = click.make_pass_decorator(GlobalConfig, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "subs"))


class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith(".py") and filename.startswith("c_"):
                rv.append(filename[2:-3])
        rv.sort()
        click.echo(rv)
        return rv

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"gli.cli.subs.c_{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


CONTEXT_SETTINGS = dict(auto_envvar_prefix="GLI")


@click.command(cls=ComplexCLI, context_settings=CONTEXT_SETTINGS)
@click.option(
    "--config",
    envvar="GLI_CONFIG",
    type=click.Path(exists=True, file_okay=False, resolve_path=True),
    help="Directory for Gli configurations.",
)
@click.option(
    "--profile",
    show_default=True,
    default="default",
    envvar="GLI_PROFILE",
    help="Profile to interact with Gitlab.",
)
@click.option("-v", "--verbose", is_flag=True, help="Enables verbose mode.")
@click.version_option(__version__)
@click.pass_context
def cli(ctx, verbose, profile, config):
    """
    Gitlab Cli.\n
    gli [--config] {repo,group,user,info,init}
    """
    ctx.obj = GlobalConfig(verbose, profile, config)


if __name__ == "__main__":
    cli()
