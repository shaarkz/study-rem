import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import pytz
from config import CHANNEL_ID, STUDY_TIME, DAYS_IN_WEEK, DURATION_TIME

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cid = CHANNEL_ID 
        self.st = STUDY_TIME
        self.dur = DURATION_TIME
        self.days = DAYS_IN_WEEK
        self.tz = pytz.timezone('America/Sao_Paulo')
        self.timer.start()

    def cog_unload(self):
        self.timer.cancel()

    @tasks.loop(seconds=60)
    async def timer(self):
        now = datetime.now(self.tz)
        at = now.strftime("%H:%M")

        print(f"[log] {at} - checking...")

        if now.weekday() not in self.days:
            return

        try:
            target = datetime.strptime(self.st, "%H:%M")
            t_min = (target - timedelta(minutes=10)).strftime("%H:%M")
            t_end = (target + timedelta(hours=self.dur)).strftime("%H:%M")
        except Exception as e:
            print(f"[error] calculation: {e}")
            return

        chan = self.bot.get_channel(self.cid)
        if not chan:
            print(f"[error] channel {self.cid} not found")
            return

        if at.endswith("0") or at.endswith("5"):
             print(f"[info] st: {self.st} | t_min: {t_min} | t_end: {t_end}")

        try:
            if at == t_min:
                print(f"[bot] sending 10min alert")
                await chan.send(f"🔔 **daq 10 minutos tropa** ajeita as coisas ai e vapo, o sofrimento começa às {self.STUDY_TIME}.\n@here")

            elif at == self.st:
                print(f"[bot] sending start alert")
                await chan.send(f"**AGORA TROPA AGORA VAO**, VEM PRA RESENHA FOCO.\n@everyone")

            elif at == t_end:
                print(f"[bot] sending end alert")
                await chan.send("✅ **Cabo guys!** Por hoje é só, podem rlx ai ja!")
                
        except discord.Forbidden:
            print("[error] missing permissions")
        except Exception as e:
            print(f"[error] {e}")

    @timer.before_loop
    async def before_timer(self):
        print("[system] waiting for readiness...")
        await self.bot.wait_until_ready()
        print("[system] timer started")

async def setup(bot):
    await bot.add_cog(Events(bot))