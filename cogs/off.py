import discord
from discord.ext import commands
from discord import app_commands

class TurnOff(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	@app_commands.command(name="off", description="Turn off the timer!")
	async def off(self, interaction: discord.Interaction):
		if not self.bot.enabled:
			await interaction.response.send_message(f'Timer is alreay off dummy!')
		else:
			self.bot.enable = False
			await interaction.response.send_message(f'Timer just turned off! {self.bot.enabled}')