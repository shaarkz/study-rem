import discord
from discord.ext import commands
from discord import app_commands

class TurnOn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="on", description="Start the timer for study")
    async def on(self, interaction: discord.Interaction):
        if self.bot.enabled:
            await interaction.response.send_message(f'The timer is already running dummy!')
        else:
            self.bot.enabled = True
            await interaction.response.send_message(f'Timer just started! {self.bot.enabled}')

async def setup(bot):
    await bot.add_cog(TurnOn(bot))
