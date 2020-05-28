from __future__ import absolute_import
from __future__ import unicode_literals

import click


@click.group()
@click.pass_obj
def cli(config):
    """
    Groups.
    """
    click.echo("calling sub cmd Groups")


@cli.command("ls", short_help="List Groups")
def ls():
    click.echo("repo list")


@cli.command("add", short_help="create Groups")
def add():
    click.echo("repo add")


@cli.command("update", short_help="update Groups")
def update():
    click.echo("repo update")


@cli.command("clone", short_help="clone Groups")
def clone():
    click.echo("repo clone")


@cli.command("desc", short_help="desc Groups")
def desc():
    click.echo("repo desc")
