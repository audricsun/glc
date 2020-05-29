from __future__ import absolute_import
from __future__ import unicode_literals

import click


@click.group()
@click.pass_obj
def cli(config):
    """
    Management for Registry.
    """
    click.echo("calling sub cmd repo")


@cli.command("ls", short_help="List Registry")
def ls():
    click.echo("repo list")


@cli.command("rm", short_help="Remove registry")
def rm():
    click.echo("Registry clone")


@cli.command("rmi", short_help="Remote image")
def rmi():
    click.echo("Registry clone")
