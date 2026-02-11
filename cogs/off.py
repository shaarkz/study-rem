import discord
from discord.ext import commands
from discord import app_commands


class TurnOff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="off",
        description="Deactivate the study timer."
    )
    async def off(self, interaction: discord.Interaction):

        state = self.bot.state

        if not state.enabled:
            await interaction.response.send_message(
                "The study timer is already disabled."
            )
            return

        state.enabled = False

        await interaction.response.send_message(
            "Study timer has been turned off."
        )


async def setup(bot):
    await bot.add_cog(TurnOff(bot))
