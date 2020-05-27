from __future__ import absolute_import
from __future__ import unicode_literals

import os

import click


class Repo(object):
    def __init__(self, home=None, debug=False):
        click.echo("INIT")
        self.home = os.path.abspath(home or ".")
        self.debug = debug


pass_repo = click.make_pass_decorator(Repo)


@click.group()
@click.option("--repo-home", envvar="REPO_HOME", default=".repo")
@click.option("--debug/--no-debug", default=False, envvar="REPO_DEBUG")
@click.pass_context
def cli(ctx, repo_home, debug):
    ctx.obj = Repo(repo_home, debug)


@cli.command()
@click.argument("src")
@click.argument("dest", required=False)
@pass_repo
def clone(repo, src, dest):
    click.echo(repo.home)


if __name__ == "__main__":
    cli()
