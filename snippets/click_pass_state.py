from __future__ import absolute_import
from __future__ import unicode_literals

import click


class State(object):
    def __init__(self):
        self.verbosity = 0
        self.debug = False


pass_state = click.make_pass_decorator(State, ensure=True)


def verbosity_option(f):
    def callback(ctx, param, value):
        state = ctx.ensure_object(State)
        state.verbosity = value
        return value

    return click.option(
        "-v",
        "--verbose",
        count=True,
        expose_value=False,
        help="Enables verbosity.",
        callback=callback,
    )(f)


def debug_option(f):
    def callback(ctx, param, value):
        state = ctx.ensure_object(State)
        state.debug = value
        return value

    return click.option(
        "--debug/--no-debug",
        expose_value=False,
        help="Enables or disables debug mode.",
        callback=callback,
    )(f)


def common_options(f):
    f = verbosity_option(f)
    f = debug_option(f)
    return f


@click.group()
def cli():
    pass


@cli.command()
@common_options
@pass_state
def cmd1(state):
    click.echo("Verbosity: %s" % state.verbosity)
    click.echo("Debug: %s" % state.debug)
