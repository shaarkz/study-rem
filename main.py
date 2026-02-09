import asyncio
import os
import discord
from discord.ext import commands
from typing import Any

try:
    from config import TOKEN 
except ImportError:
    raise ImportError("create a config.py file with the TOKEN variable(with your token)")

class Bot(commands.Bot):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
                print(f"✔ Cog {filename} loaded!")
        
        await self.tree.sync()

intents = discord.Intents.default()
intents.message_content = True

bot = Bot(
    command_prefix="n.",
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    print(f"Bot working as {bot.user}")

async def main():
    async with bot:
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())