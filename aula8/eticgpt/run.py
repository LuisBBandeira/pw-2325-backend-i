import click
from eticgpt import bot as etic_bot

@click.group()
def bot():
    pass

@bot.command()
@click.Option('--token',show_envvar="BOT_TOKEN")
def run(token:str):
    etic_bot.client.run(token) 


if __name__ == "__main__":
    bot(auto_envvar_prefix="ETIC")