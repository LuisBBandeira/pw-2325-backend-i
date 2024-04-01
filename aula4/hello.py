import click

@click.command()
@click.option("--name", prompt="Your name", help="The person to greet.")
def run(name):
        click.echo(f"hi, {name}!")

if __name__ == '__main__':
    run()