from __future__ import absolute_import
from __future__ import unicode_literals

import click

from gli.cli.entry import pass_environment


# @click.command("project", short_help="Projects.")
@click.group()
@pass_environment
def cli(ctx):
    """
    Management for repository.
    """
    ctx.log("Changed files: none")
    ctx.vlog("bla bla bla, debug info")


@cli.command("ls", short_help="List repositories")
def ls():
    click.echo("Running list")


@cli.command("create", short_help="create repositories")
def create():
    click.echo("Running list")


@cli.command("update", short_help="update repositories")
def update():
    click.echo("Running list")


@cli.command("clone", short_help="clone repositories")
def clone():
    click.echo("Running list")


@cli.command("desc", short_help="desc repositories")
def desc():
    click.echo("Running list")
