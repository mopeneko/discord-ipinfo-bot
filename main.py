import json
import os

from discord.ext import commands
import requests

bot = commands.Bot(command_prefix=".")


@bot.command()
async def ip(ctx, arg):
    res = requests.get(f"https://ipinfo.io/{arg}")
    data = res.json()
    pretty_data = json.dumps(data, indent=4)
    await ctx.send(f"```json\n{pretty_data}\n```")


bot.run(os.getenv("DISCORD_TOKEN"))
