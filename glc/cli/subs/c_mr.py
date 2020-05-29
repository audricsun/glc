from __future__ import absolute_import
from __future__ import unicode_literals

import click


@click.group()
@click.pass_obj
def cli(config):
    """
    Merge Requests.
    """
    click.echo("calling sub cmd repo")


@cli.command("ls", short_help="List MR")
def ls():
    click.echo("repo list")


@cli.command("add", short_help="Create merge request from current repo")
def add():
    click.echo("repo add")


@cli.command("update", short_help="update MR")
def update():
    click.echo("repo update")


@cli.command("status", short_help="Show status repo")
def status():
    click.echo("repo desc")
