import click

@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    if 'items' not in ctx.obj:
        ctx.obj['items'] = []

@cli.command()
@click.pass_obj
def show(obj):
    for idx, item in enumerate(obj['items']):
        print(f"{idx+1}. {item}")

@cli.command()
@click.pass_obj
@click.argument("name")
def add(obj, name):
    obj['items'].append(name)
    print(f"Item added: {name}")

@cli.command()
@click.pass_obj
@click.argument("name")
def rm(obj, name):
    if name in obj['items']:
        obj['items'].remove(name)
        print(f"Item removed: {name}")
    else:
        print(f"Item '{name}' not found.")

if __name__ == "__main__":
    cli(obj={})
