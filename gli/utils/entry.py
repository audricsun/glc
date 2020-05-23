from __future__ import absolute_import
from __future__ import unicode_literals

import click


@click.group()
# @click.version_option(VERSION)
@click.pass_context
def cli(version):
    """
    Cerberus Commandline interface entrypoint.
    """
    pass


@cli.command()
def project():
    pass


def group():
    pass


def user():
    pass


if __name__ == "__main__":
    cli()
