import discord

# This will load the permissions the bot has been granted in the previous configuration
intents = discord.Intents.default()
intents.message_content = True

class aclient(discord.Client):
  def __init__(self):
    super().__init__(intents = intents)
    self.added = False

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.added:
      self.added = True
    print(f"Say hi to {self.user}!")

client = aclient()

@client.event
async def on_message(message):
  # This checks if the message is not from the bot itself. If it is, it'll ignore the message.
  if message.author == client.user:
    return

  # From here, you can add all the rules and the behaviour of the bot.
  # In this case, the bot checks if the content of the message is "Hello!" and send a message if it's true.
  if message.content == 'Hello!':
    await message.channel.send("Hello! I'm happy to see you around here.")
    return

  if message.content == 'Good bye!':
    await message.channel.send("Hope to see you soon!")
    return


# add the token of your bot
client.run('your-bot-token-here')