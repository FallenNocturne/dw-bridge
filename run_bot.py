import discord
import config

bot = discord.Bot()

@bot.event
async def on_ready():
    print("Logged in as",bot.user)
    print("Active in",", ".join([guild.name for guild in bot.guilds]))

@bot.slash_command(guild_ids=[config.guild_id],name="hello",description="returns hello")
async def hello(ctx):
    await ctx.respond("hello")

bot.run(config.bot_token)