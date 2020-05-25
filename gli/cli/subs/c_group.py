from __future__ import absolute_import
from __future__ import unicode_literals

import click

from gli.cli.entry import pass_environment


@click.command("group", short_help="Groups.")
@pass_environment
def cli(ctx):
    """Shows file changes in the current working directory."""
    ctx.log("Changed files: none")
    ctx.vlog("bla bla bla, debug info")
