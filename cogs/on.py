import discord
from discord.ext import commands
from discord import app_commands


class TurnOn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="on",
        description="Activate the study timer."
    )
    async def on(self, interaction: discord.Interaction):
    
        state = self.bot.state
    
        if not state.channel_id or not state.study_time or not state.duration_time:
            await interaction.response.send_message(
                "You must configure the timer first using /set.",
                ephemeral=True
            )
            return
    
        if state.enabled:
            await interaction.response.send_message(
                "The study timer is already running.",
                ephemeral=True
            )
            return
    
        state.enabled = True
    
        await interaction.response.send_message(
            "Study timer activated successfully."
        )


async def setup(bot):
    await bot.add_cog(TurnOn(bot))
