from __future__ import absolute_import
from __future__ import unicode_literals

import click


@click.command("user", short_help="Get/List/Update user and groups.")
@click.pass_obj
def cli(config):
    """Shows file changes in the current working directory."""
    click.entry("Calling sub user")
