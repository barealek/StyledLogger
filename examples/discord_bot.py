##
# An example showing one way of using StyledLogger with a discord.py bot.
##


from styledlogger import StyledLogger
import discord

bot = discord.Client()
bot.logger = StyledLogger("discord")

@bot.event
async def on_ready():
    bot.logger.info("Logged in!")

@bot.event
async def on_message(message):
    bot.logger.debug("Message received!")
    if message.content == "ping":
        await message.channel.send("pong")

bot.logger.info("Starting bot...")
bot.run(...)