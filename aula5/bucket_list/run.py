import click

filename = "COMPRAS.txt"

@click.group()
def cli():
    pass

@cli.command()
def show():
    with open(filename, 'r') as file:
        for idx, line in enumerate(file, start=1):
            print(f"{idx}. {line.strip()}")

@cli.command()
@click.argument("name")
def add(name):
    items = {}
    with open(filename, 'r') as file:
        for line in file:
            item = line.strip()
            if '(' in item:
                item_name, count = item.split(' (')
                count = int(count[:-1])
                items[item_name] = count
            else:
                items[item] = 1

    if name in items:
        count = items[name] + 1
        items[name] = count
        print(f"Item '{name}' already exists. Counter incremented to {count}.")
    else:
        count = 1
        items[name] = count
        print(f"Item added: {name}")

    with open(filename, 'w') as file:
        for item, count in items.items():
            file.write(f"{item} ({count})\n")

@cli.command()
@click.argument("name")
def rm(name):
    items = {}
    with open(filename, 'r') as file:
        for line in file:
            item = line.strip()
            if '(' in item:
                item_name, count = item.split(' (')
                count = int(count[:-1])
                items[item_name] = count
            else:
                items[item] = 1

    if name in items:
        count = items[name]
        if count > 1:
            items[name] -= 1
        else:
            del items[name]

        with open(filename, 'w') as file:
            for item, count in items.items():
                file.write(f"{item} ({count})\n")
        print(f"Item removed: {name}")
    else:
        print(f"Item '{name}' not found.")

if __name__ == "__main__":
    cli()
