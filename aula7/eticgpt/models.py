import click



@click.group()
def bot():
    pass


@bot.command()
def run():
    gpt_bot.start()


if __name__ == "__main__":
    bot()