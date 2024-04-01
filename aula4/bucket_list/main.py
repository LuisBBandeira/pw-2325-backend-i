import click


@click.group
@click.pass_content
def cli(li):
    li.ensure_object(list)

@cli.command()
@click.argument("name")
@click.pass_context
def add(li , name:str):
    li.obj.append(name)


if __name__ == "__main__":
    
    