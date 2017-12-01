#!/usr/bin/env python3
import sys

import click

from mpparser import MowerProgramParser, MowerProgramParseError


@click.command()
@click.argument('program')
def mower(program):
    """
    Run the mower simulation whose instructions are in PROGRAM file.
    """
    try:
        parser = MowerProgramParser(open(program, 'r'))
    except MowerProgramParseError as e:
        click.secho('failed to parse program with error: {}'.format(e), fg='red', err=True)
        sys.exit(255)

    mowers = parser.mowers
    lawn = parser.lawn
    mowers_set = set(mowers)

    for step in range(max([len(m.program) for m in mowers])):
        for mower in mowers:
            mower.do_next_step(
                lawn=lawn,
                others=mowers_set - {mower},
            )

    for mower in parser.mowers:
        click.echo(str(mower))


if __name__ == '__main__':
    mower()