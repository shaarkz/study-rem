import asyncio
import os
import discord
from discord.ext import commands
from typing import Any
from data.state import State

try:
    from config import TOKEN
except ImportError:
    raise ImportError(
        "Create a config.py file containing your TOKEN variable."
    )


class Bot(commands.Bot):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
                print(f"✔ Loaded cog: {filename}")

        await self.tree.sync()


intents = discord.Intents.default()
intents.message_content = True

bot = Bot(
    command_prefix="n.",
    intents=intents,
    help_command=None
)

bot.state = State(
    enabled=False,
    channel_id=None,
    study_time=None,
    duration_time=None,
    schedule={}
)


@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")


async def main():
    async with bot:
        await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
