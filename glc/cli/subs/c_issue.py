from __future__ import absolute_import
from __future__ import unicode_literals

import click


@click.group()
@click.pass_obj
def cli(config):
    """
    Issues.
    """
    click.echo("calling sub cmd repo")


@cli.command("ls", short_help="List MR")
def ls():
    click.echo("repo list")


@cli.command("add", short_help="create MR")
def add():
    click.echo("repo add")


@cli.command("update", short_help="update MR")
def update():
    click.echo("repo update")


@cli.command("top", short_help="charts for MRs")
def top():
    click.echo("repo desc")
