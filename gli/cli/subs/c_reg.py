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


@cli.command("ls", short_help="List repositories")
def ls():
    click.echo("repo list")


@cli.command("add", short_help="create repositories")
def add():
    click.echo("repo add")


@cli.command("update", short_help="update repositories")
def update():
    click.echo("repo update")


@cli.command("clone", short_help="clone repositories")
def clone():
    click.echo("repo clone")


@cli.command("desc", short_help="desc repositories")
def desc():
    click.echo("repo desc")


@cli.group()
@click.pass_obj
def reg(config):
    """
    Registry of Repository.
    """
    pass


@reg.command("ls")
def ls_reg():
    pass
