import discord
import config
import re

bot = discord.Bot()

@bot.event
async def on_ready():
    print("Logged in as",bot.user)
    print("Active in",", ".join([guild.name for guild in bot.guilds]))

@bot.slash_command(guild_ids=[config.guild_id],name="hello",description="returns hello")
async def hello(ctx):
    await ctx.respond("hello")

@bot.slash_command(guild_ids=[config.guild_id],name="register",description="DM registration of mobile number")
async def register(ctx):
    await ctx.respond("Sending you a DM...")
    await ctx.author.send("Hello. Please send the word 'REGISTER', then your phone number\nAs in: *REGISTER <phone_no>*")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if not message.guild:
        msg_text = message.content
        msg_text = msg_text.split(" ")
        if msg_text[0].upper() == "REGISTER":
            phone_num = msg_text[1]
            if re.match("[+]?\d+",phone_num):
                await message.channel.send("Successfully registered number")
                print(phone_num)
            else:
                await message.channel.send("Invalid phone number")
        else:
            await message.channel.send("Invalid command. Use 'REGISTER <phone_no>' to register")
    else:
        await message.channel.send("This was not from a DM")


bot.run(config.bot_token)