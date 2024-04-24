import click

@click.group
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj['items'] = []

@cli.command()

def show():
    ctx = click.get_current_context()
    items = ctx.obj['items']
    print("Itens da lista")
    for item in items:
        print(item)


@cli.command()
@click.argument("name")
def add(ctx ,name:str):
    ctx = click.get_current_context()
    ctx.obj['items'].append(name)
    print(f"{name.upper()} added!")

if __name__== "__main__":

    cli()

