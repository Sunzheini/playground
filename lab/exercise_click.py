"""
Click is a Python package for creating beautiful and composable command-line interfaces
(CLIs). Its main goal is to make the process of writing command-line tools quick, easy,
and enjoyable without requiring any extra "magic."
"""
import click


@click.command()                                                                           # 2. Decorate to make it a CLI command
@click.option('--name', '-n', default='World', help='The person to greet.')     # 3. Add an option
@click.option('--count', '-c', default=1, help='Number of greetings.')          # 4. Add another option
def hello(name, count):                                                                    # 5. The function that does the work
    """This script greets YOU!"""                                                          # 6. The docstring becomes the help description
    for _ in range(count):  #
        click.echo(f"Hello, {name}!")


if __name__ == '__main__':
    hello()
"""
python lab/exercise_click.py --name Alice       → "Hello, Alice!"
python lab/exercise_click.py -n Alice -c 3      → "Hello, Alice!" printed 3 times.
python lab/exercise_click.py --help                 → Automatically generates a beautiful help page:
"""