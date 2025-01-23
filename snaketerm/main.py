import curses
from .game import Game
import click
from . import VERSION_STRING

def play(stdscr):
    game = Game(stdscr)
    game.run()
def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(VERSION_STRING)
    ctx.exit()
@click.command()
@click.option("-v", "--version", is_flag=True, callback=print_version,expose_value=False, is_eager=True, help="Show version and exit")
def main():
    curses.wrapper(play)
    
# if __name__ == '__main__':
#     main()
    
