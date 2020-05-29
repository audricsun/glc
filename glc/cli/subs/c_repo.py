from __future__ import absolute_import
from __future__ import unicode_literals

import click


@click.group()
@click.pass_obj
def cli(config):
    """
    Management for repository.
    """
    click.echo("calling sub cmd repo")


@cli.command("ls", short_help="List repositories")
def ls():
    click.echo("repo list")


@cli.command("create", short_help="Create new repositories")
def create():
    click.echo("repo create")


@cli.command("update", short_help="update repositories")
def update():
    click.echo("repo update")


@cli.command("clone", short_help="clone repositories")
def clone():
    click.echo("repo clone")


@cli.command("desc", short_help="desc repositories")
def desc():
    click.echo("repo desc")
