from __future__ import absolute_import
from __future__ import unicode_literals

import click


@click.command("info", short_help="Display Information.")
@click.pass_obj
def cli(config):
    """Show current configuration information."""
    click.echo("calling sub cmd info")
    click.echo(f"Profile: {config.profile} Config Path: {config.config}")
