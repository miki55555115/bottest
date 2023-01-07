import nextcord
from nextcord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        channel = self.bot.get_channel(1061270416640974888) or await self.bot.fetch_channel(1061270416640974888)
        await channel.send(f"{member.mention} joined the **{channel.guild.name}**")
        
    @commands.command(name="echo")
    async def _echo(self, ctx: commands.Context, *, msg: str):
        await ctx.channel.send(msg)

def setup(bot):
    bot.add_cog(Commands(bot))