import click
from eticgpt import bot as etic_bot

@click.group()
def bot():
    pass

@bot.command()
def start():
    etic_bot.client.start("TOKEN Here") 


if __name__ == "__main__":
    bot(auto_envvar_prefix="ETIC")