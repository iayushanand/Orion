import discord
from discord.ext import commands


class Vocals(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.logger = bot.logger
        self.bot = bot
    
    @commands.command(name = "join", aliases = ["j"])
    async def join(self, ctx: commands.Context):
        vc = ctx.author.voice
        if not vc:
            return await ctx.reply("You are not connected to a voice channel!")
        await vc.channel.connect()
        await ctx.reply(f"Connected to VC: {vc.channel.mention}")
        self.logger.info(f"Joined voice channel - {vc.channel.name}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Vocals(bot=bot))