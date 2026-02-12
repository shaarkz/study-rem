import discord
from discord.ext import commands
from discord import app_commands


DEFAULT_CHANNEL_ID = 1470468503323803830
DEFAULT_DURATION = 2

DEFAULT_WEEK_SCHEDULE = {
    0: "18:00",  # Monday
    1: "19:00",  # Tuesday
    2: "18:30",  # Wednesday
    3: "14:09",  # Thursday
    4: "17:30",  # Friday
    5: "16:00",  # Saturday
    6: "15:30",  # Sunday
}


class Default(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="default",
        description="Apply the predefined weekly study schedule."
    )
    async def default(self, interaction: discord.Interaction):
        state = self.bot.state

        state.channel_id = DEFAULT_CHANNEL_ID
        state.duration_time = DEFAULT_DURATION
        state.week_schedule = DEFAULT_WEEK_SCHEDULE.copy()
        state.enabled = True

        print("[SYSTEM] Default weekly schedule applied.")
        print(f"[SYSTEM] Schedule: {DEFAULT_WEEK_SCHEDULE}")

        await interaction.response.send_message(
            "📅 **Weekly schedule activated successfully!**\n"
            "Different study times configured for each weekday.\n"
            "The study system is now enabled."
        )


async def setup(bot):
    await bot.add_cog(Default(bot))
