# SPDX-FileCopyrightText: 2023-present Alvaro Leiva Geisse <aleivag@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from dumas.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="dumas")
def dumas():
    click.echo("Hello world!")
