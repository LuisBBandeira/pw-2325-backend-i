import click
from eticgpt import bot as chat_bot
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@click.group()
def bot():
    logger.error("bot Started")


@bot.command()
@click.option('--token', envvar="BOT_TOKEN",show_envvar=True, type=str)
def run(token:str):
    logger.info("RUN Command started")
    chat_bot.client.run(token)


if __name__ == "__main__":
    bot()