import click
import os

filename = "COMPRAS.txt"

@click.command()
def hello():
    click.echo("Hello" , color =True)

@click.command()
@click.argument("product")

def add(product:str):
        file =open(filename , "a")
        file.write(f"{product}\n" )
        file.close()
        click.echo(f"{product.upper()} added!")
        


if __name__ == "__main__":
    hello()
    