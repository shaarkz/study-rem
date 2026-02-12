import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import pytz


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tz = pytz.timezone("America/Sao_Paulo")
        self.timer.start()

    def cog_unload(self):
        self.timer.cancel()

    @tasks.loop(minutes=1)
    async def timer(self):
        state = self.bot.state
        now = datetime.now(self.tz)
        current_time = now.strftime("%H:%M")
        today = now.date()
        weekday = now.weekday()

        if not state.enabled:
            return

        if not state.channel_id or not state.duration_time:
            return

        if weekday not in state.week_schedule:
            return

        study_time = state.week_schedule[weekday]

        print(f"[TIMER] {current_time} | Checking schedule for weekday {weekday}")

        try:
            target_time = datetime.strptime(study_time, "%H:%M")

            ten_minutes_before = (
                target_time - timedelta(minutes=10)
            ).strftime("%H:%M")

            end_time = (
                target_time + timedelta(hours=state.duration_time)
            ).strftime("%H:%M")

        except Exception as e:
            print(f"[ERROR] Time calculation failed: {e}")
            return

        channel = self.bot.get_channel(state.channel_id)

        if not channel:
            print(f"[ERROR] Channel ID {state.channel_id} not found.")
            return

        try:
            if current_time == ten_minutes_before:
                if state.last_reminder_date == today:
                    return

                state.last_reminder_date = today

                print("[EVENT] Sending 10-minute reminder.")
                await channel.send(
                    f"🔔 **Faltam 10 minutos para o estudo!**\n"
                    f"Prepare seu material. Se ajeita ai mancho.\n"
                    f"Início às **{state.study_time}**.\n@here"
                )

            elif current_time == study_time:
                if state.last_start_date == today:
                    return

                state.last_start_date = today

                print("[EVENT] Sending study start message.")
                await channel.send(
                    "**Hora de estudar!** 📚\n"
                    "Foco total agora, **PODEMOS MUITO PODEMOS MAIS**.\n@everyone"
                )

            elif current_time == end_time:
                if state.last_end_date == today:
                    return

                state.last_end_date = today

                print("[EVENT] Sending study end message.")
                await channel.send(
                    "**Sessão finalizada!**\n"
                    "Bom trabalho hoje."
                )

        except discord.Forbidden:
            print("[ERROR] Missing permission to send messages.")
        except Exception as e:
            print(f"[ERROR] Unexpected error: {e}")

    @timer.before_loop
    async def before_timer(self):
        print("[SYSTEM] Waiting for bot readiness...")
        await self.bot.wait_until_ready()
        print("[SYSTEM] Background timer loop initialized.")
        print("[SYSTEM] Study system is currently DISABLED.")


async def setup(bot):
    await bot.add_cog(Events(bot))
