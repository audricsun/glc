from __future__ import absolute_import
from __future__ import unicode_literals

import click


@click.command("user", short_help="Namespace management.")
@click.pass_obj
def cli(config):
    """
    Management gitlab namespaces.
    """
    click.entry("Calling sub user")
