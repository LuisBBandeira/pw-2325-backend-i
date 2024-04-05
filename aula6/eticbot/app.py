import click
from eticbot import bot as discord_bot

@click.group()
def bot():
    pass

    
# @click.option("-g","--guildID","guild_id")
@bot.command()
def start():
    discord_bot.client.run("TOKEN Here") 


if __name__ == "__main__":
    bot(auto_envvar_prefix="ETIC")