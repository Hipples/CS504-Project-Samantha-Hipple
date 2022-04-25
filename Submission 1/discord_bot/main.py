import discord 
import os

client = discord.Client()

@client.event # register an event 
async def on_ready(): # called when bot is ready
    print("We have logged in as {0.user}".format(client)) # displays username

@client.event
async def on_message(message): # called by message
  if message.author == client.user:
    return # do not respond to own messages

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
    # bot responds to $hello with Hello!

client.run(os.getenv('TOKEN'))
# bot password as env variable