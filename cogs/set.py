import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime


class Set(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="set",
        description="Configure the study timer. Example: /set #channel 18:30 2(hours)"
    )
    async def set(
        self,
        interaction: discord.Interaction,
        channel: discord.TextChannel,
        study_time: str,
        duration: int
    ):
        state = self.bot.state

        try:
            datetime.strptime(study_time, "%H:%M")
        except ValueError:
            await interaction.response.send_message(
                "Invalid time format. Use HH:MM (example: 18:30).",
                ephemeral=True
            )
            return

        if duration <= 0:
            await interaction.response.send_message(
                "Duration must be greater than 0 (in hours).",
                ephemeral=True
            )
            return

        state.channel_id = channel.id
        state.study_time = study_time
        state.duration_time = duration

        await interaction.response.send_message(
            f"✅ **Study timer configured!**\n\n"
            f"Channel: {channel.mention}\n"
            f"Start time: {study_time} (24h format)\n"
            f"Duration: {duration} hour(s)\n\n"
            f"Now use `/on` to activate it."
        )


async def setup(bot):
    await bot.add_cog(Set(bot))
