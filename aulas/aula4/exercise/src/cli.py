import click

@click.group
@click.pass_context
def cli(ctx):
    ctx.ensure_object(list)

@cli.command()
@click.pass_context

def show(ctx):
    print(ctx.get('cenas'))

@cli.command()
@click.argument("name")
def add(ctx ,name:str):
    ctx.obj.append(name)
    print(f"{name.upper()} added!")

if __name__== "__main__":

    add()
    show()
