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

    @tasks.loop(seconds=30)
    async def timer(self):
        state = self.bot.state
        now = datetime.now(self.tz)
        current_time = now.strftime("%H:%M")

        if not state.enabled:
            return

        print(f"[TIMER] {current_time} | Checking schedule...")

        # if now.weekday() not in state.days_in_week:
        #     return

        try:
            target_time = datetime.strptime(state.study_time, "%H:%M")
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

        if current_time.endswith(("0", "5")):
            print(
                f"[INFO] Study: {state.study_time} | "
                f"Reminder: {ten_minutes_before} | "
                f"End: {end_time}"
            )

        try:
            if current_time == ten_minutes_before:
                print("[EVENT] Sending 10-minute reminder.")
                await channel.send(
                    f"🔔 **Faltam 10 minutos para o estudo!**\n"
                    f"Organize seu material e agiliza ai mancho.\n"
                    f"Começa às **{state.study_time}**.\n@here"
                )

            elif current_time == state.study_time:
                print("[EVENT] Sending study start message.")
                await channel.send(
                    "**Hora de estudar!**\n"
                    "Foco total agora. PODEMOS MUITO PODEMOS MAIS.\n@everyone"
                )

            # Fim do estudo
            elif current_time == end_time:
                print("[EVENT] Sending study end message.")
                await channel.send(
                    "**Sessão finalizada!**\n"
                    "Bom trabalho hoje. Descansem!"
                )

        except discord.Forbidden:
            print("[ERROR] Missing permissions to send messages.")
        except Exception as e:
            print(f"[ERROR] Unexpected error: {e}")

    @timer.before_loop
    async def before_timer(self):
        print("[SYSTEM] Waiting for bot readiness...")
        await self.bot.wait_until_ready()
        print("[SYSTEM] Timer successfully started.")


async def setup(bot):
    await bot.add_cog(Events(bot))
