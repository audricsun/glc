from __future__ import absolute_import
from __future__ import unicode_literals

import click


@click.group()
@click.pass_obj
def cli(config):
    """
    Snippets.
    """
    click.echo("calling sub cmd repo")


@cli.command("ls", short_help="List Snippets")
def ls():
    click.echo("Snippets list")


@cli.command("add", short_help="create Snippets")
def add():
    click.echo("Snippets add")


@cli.command("update", short_help="update Snippets")
def update():
    click.echo("Snippets update")
