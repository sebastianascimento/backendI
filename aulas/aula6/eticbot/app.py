import click

@click.group()
def bot():
    pass

@bot.command()
@click.option("-g" "--guildID" , "guild_id")
@click.option("-t" , "--token")
def start(guild_id: str , token:str):
    pass

if __name__ == "__main__":
    