import click

class Config():
    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure = True)

@click.group()
@click.option('--verbose', is_flag = True)
@pass_config
def cli(config, verbose):
    config.verbose = verbose

@cli.command()
@click.option('--string', '-s', default = 'world')
@click.argument('out', type = click.File('w'), default = '-')
@pass_config
def say(config, string, out):
    """Example script."""
    if config.verbose:
        click.echo('in verbose mode')
    out.write('Hello %s!\n' % string)