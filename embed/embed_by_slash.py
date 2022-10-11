import discord

# This will load the permissions the bot has been granted in the previous configuration
intents = discord.Intents.default()
intents.message_content = True

class aclient(discord.Client):
  def __init__(self):
    super().__init__(intents = intents)
    self.synced = False # added to make sure that the command tree will be synced only once

  async def on_ready(self):
    await self.wait_until_ready()

    if not self.synced: #check if slash commands have been synced 
      await tree.sync(guild = discord.Object(id='your-server-id-here')) #guild specific: you can leave sync() blank to make it global. 
      # But it can take up to 24 hours, so test it in a specific guild.
      self.synced = True

    print(f"Say hi to {self.user}!")

client = aclient()
tree = discord.app_commands.CommandTree(client)


@tree.command(name='greet-other-lang-in', guild=discord.Object(id='your-server-id-here'), description='Show greeting buttons.')
async def send_embed(interaction: discord.Interaction):
  embed = discord.Embed(title='Greetings in other languages', 
    description='Learn how to greet in other languages!', 
    color=13636871,
    url='https://www.rosettastone.com/languages/good-morning-in-a-different-language')
  embed.set_thumbnail(url='https://duoplanet.com/wp-content/uploads/2021/06/All-Duolingo-Languages-1250x703.png') # image by Duolingo
  embed.set_author(name="fumiow", url='https://www.linkedin.com/in/leandro-fumio-kino-17358191/', icon_url='https://media-exp1.licdn.com/dms/image/C4D03AQE_dGYm5nzVyA/profile-displayphoto-shrink_200_200/0/1583970394645?e=1671062400&v=beta&t=sRtguPB6hO7ZLWjjZT6focIl6ozJrjOPdKJ3EqoH1jE')
  embed.set_image(url='https://media-exp1.licdn.com/dms/image/C5616AQFK4y0nyzx7lA/profile-displaybackgroundimage-shrink_350_1400/0/1622324906380?e=1671062400&v=beta&t=p3xVBxCLJ1zi1I4cE2WX8iCcjcOBXPPZKKYANAq2Jbw')
  embed.add_field(name='English', value='Good morning!', inline=True)
  embed.add_field(name='Portuguese', value='Bom dia!', inline=True)
  embed.add_field(name='Spanish', value='¡Buenos dias!', inline=True)
  embed.add_field(name='Japanese', value='おはようございます。', inline=True)
  embed.set_footer(text='It\'s nice to see you again')

  await interaction.response.send_message(embed=embed)


@tree.command(name='greet-inline-1', guild=discord.Object(id='your-server-id-here'), description='Show greeting buttons.')
async def send_embed(interaction: discord.Interaction):
  embed = discord.Embed(title='Greetings in other languages', 
    description='Learn how to greet in other languages!')
  embed.add_field(name='English', value='Good morning!', inline=True)
  embed.add_field(name='Portuguese', value='Bom dia!', inline=True)
  embed.add_field(name='Spanish', value='¡Buenos dias!', inline=True)
  embed.add_field(name='Japanese', value='おはようございます。', inline=True)

  await interaction.response.send_message(embed=embed)


@tree.command(name='greet-inline-2', guild=discord.Object(id='your-server-id-here'), description='Show greeting buttons.')
async def send_embed(interaction: discord.Interaction):
  embed = discord.Embed(title='Greetings in other languages', 
    description='Learn how to greet in other languages!')
  embed.add_field(name='English', value='Good morning!', inline=False)
  embed.add_field(name='Portuguese', value='Bom dia!', inline=False)
  embed.add_field(name='Spanish', value='¡Buenos dias!', inline=False)
  embed.add_field(name='Japanese', value='おはようございます。', inline=False)

  await interaction.response.send_message(embed=embed)


@tree.command(name='greet-inline-3', guild=discord.Object(id='your-server-id-here'), description='Show greeting buttons.')
async def send_embed(interaction: discord.Interaction):
  embed = discord.Embed(title='Greetings in other languages', 
    description='Learn how to greet in other languages!')
  embed.add_field(name='Language', value='English\nPortuguese\nSpanish\nJapanese', inline=True)
  embed.add_field(name='How to say', value='Good morning!\nBom dia!\n¡Buenos dias!\nおはようございます。', inline=True)

  await interaction.response.send_message(embed=embed)

# add the token of your bot
client.run('your-bot-token-here')