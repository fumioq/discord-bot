import discord
from enum import Enum

# This will load the permissions the bot has been granted in the previous configuration
intents = discord.Intents.default()
intents.message_content = True

class aclient(discord.Client):
  def __init__(self):
    super().__init__(intents = intents)
    self.synced = False # added to make sure that the command tree will be synced only once
    self.added = False

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.synced: #check if slash commands have been synced 
      await tree.sync(guild = discord.Object('your-server-id-here')) #guild specific: you can leave sync() blank to make it global. But it can take up to 24 hours, so test it in a specific guild.
      self.synced = True
    if not self.added:
      self.added = True
    print(f"Say hi to {self.user}!")

client = aclient()
tree = discord.app_commands.CommandTree(client)

@tree.command(description='Respond hello to you.', guild=discord.Object('your-server-id-here'))
async def greet(interaction: discord.Interaction):
  await interaction.response.send_message('Hello!')


@tree.command(description='Respond hello to you and mention yout user.', guild=discord.Object('your-server-id-here'))
async def greet_user(interaction: discord.Interaction):
  user = interaction.user.id
  await interaction.response.send_message(f'Hello, <@{user}>!')

GreetingTime = Enum(value='GreetingTime', names=['MORNING', 'AFTERNOON', 'EVENING', 'NIGHT'])

@tree.command(description='Respond according to the period of the day.', guild=discord.Object('your-server-id-here'))
@discord.app_commands.describe(period='Period of the day')
async def greet_user_time_of_the_day(interaction: discord.Interaction, period: GreetingTime):
  user = interaction.user.id
  if period.name == 'MORNING':
    await interaction.response.send_message(f'Good Morning, <@{user}>!')
    return
  if period.name == 'AFTERNOON':
    await interaction.response.send_message(f'Good Afternoon, <@{user}>!')
    return
  if period.name == 'EVENING':
    await interaction.response.send_message(f'Good Evening, <@{user}>!')
    return
  if period.name == 'NIGHT':
    await interaction.response.send_message(f'Have a good night, <@{user}>!')
    return



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
# client.run('your-bot-token-here')