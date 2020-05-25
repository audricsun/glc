from __future__ import absolute_import
from __future__ import unicode_literals

import click


@click.group()
# @click.version_option(VERSION)
@click.pass_context
def entry(version):
    """
    Gitlab command line interface.
    """
    pass


@entry.command()
def init():
    """
    Initialize gli configuration files.
    """
    pass


@entry.command()
def fetch():
    """
    Read from remote Gitlab server, and update local configuration files.
    """
    pass


@entry.command()
def push():
    """
    Push change sets from local configuration to remote Gitlab server.
    """
    pass


@entry.command()
def project():
    pass


@entry.command()
def group():
    pass


@entry.command()
def user():
    pass


if __name__ == "__main__":
    entry()
