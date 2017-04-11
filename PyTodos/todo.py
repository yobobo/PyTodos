# -*- coding: utf-8 -*-

import click


@click.group(context_settings={'help_option_names': ('-h', '--help')})
def cli():
    pass


@cli.command()
def add(task_detail):
    print task_detail
    print 'task added.'


@cli.command()
def kill():
    print 'killed'
