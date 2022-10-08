import discord

# This will load the permissions the bot has been granted in the previous configuration
intents = discord.Intents.default()
intents.message_content = True

class aclient(discord.Client):
  def __init__(self):
    super().__init__(intents = intents)
    self.added = False # added to make sure that the views will be synced only once
    self.synced = False # added to make sure that the command tree will be synced only once

  async def on_ready(self):
    await self.wait_until_ready()

    if not self.added:
      self.add_view(greet_view()) # add view to the Bot
      self.added = True

    if not self.synced: #check if slash commands have been synced 
      await tree.sync(guild = discord.Object(id='your-guild-id')) #guild specific: you can leave sync() blank to make it global. 
      # But it can take up to 24 hours, so test it in a specific guild.
      self.synced = True


    print(f"Say hi to {self.user}!")

client = aclient()
tree = discord.app_commands.CommandTree(client)

class greet_view(discord.ui.View):
  # View has a timeout of 180 seconds (3 minutes). The 2 lines of code below  timeout 
  def __init__(self) -> None:
      super().__init__(timeout=None)


  # First button - Just an Emoji, default color
  @discord.ui.button(custom_id = "emoji_button", emoji= '\U0001F606')
  async def say_hello(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(f'Hello!')


  # You can add up to 25 buttons to the same view, but make sure it's custom_id and function name are always different!
  # Second button - Label 'greet', green, no emoji
  @discord.ui.button(label='greet', custom_id = "greet_button", style = discord.ButtonStyle.blurple)
  async def greet_user(self, interaction: discord.Interaction, button: discord.ui.Button):
    user = interaction.user.id
    await interaction.response.send_message(f'Hello, <@{user}>, how are you doing today?')


  # Third button - Label 'say goodbye', red, has emoji
  @discord.ui.button(label='say goodbye', custom_id = "good_bye_button", emoji = '\U0001F601', style = discord.ButtonStyle.red)
  async def say_goodbye_to_user(self, interaction: discord.Interaction, button: discord.ui.Button):
    user = interaction.user.id
    await interaction.response.send_message(f'Good bye, <@{user}>, hope to see you soon!')


@tree.command(name='greet-buttons', guild=discord.Object(id='your-guild-id'), description='Show greeting buttons.')
async def show_view(interaction: discord.Interaction):
  await interaction.response.send_message(view=greet_view())

@tree.command(name='greet-buttons-with-text', guild=discord.Object(id='your-guild-id'), description='Show greeting buttons with text.')
async def show_view_with_text(interaction: discord.Interaction):
  await interaction.response.send_message("Hi! What you would like me to do?", view=greet_view())


# add the token of your bot
client.run('your-bot-token-here')