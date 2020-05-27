from __future__ import absolute_import
from __future__ import unicode_literals

import click

from gli.config.conf import GitlabConfigFile


@click.group()
@click.pass_obj
def cli(config):
    """
    Configuration files and bulk update.
    """
    if config.verbose:
        click.echo("calling sub cmd repo group")


@cli.command("init", short_help="Initialize config files.")
@click.pass_obj
def init(config):
    """
    Initialize config files.
    """
    click.echo(click.style("Initializing configuration files.", fg="green"))
    click.echo(config.config)
    file = GitlabConfigFile(config.config)
    if not file.exist and click.confirm("Do you want to create one?"):
        file.init()


@cli.command("ls", short_help="List configuration files.")
def ls():
    click.echo("repo list")


@cli.command("add", short_help="Add configuration files.")
def add():
    click.echo("repo add")


@cli.command("pull", short_help="Update configuration files from remote.")
def pull():
    click.echo("repo update")


@cli.command("push", short_help="Push configuration changes from local to remote.")
def push():
    click.echo("repo clone")


@cli.command("desc", short_help="Describe configuration file.")
def desc():
    click.echo("repo desc")
