import discord

# This will load the permissions the bot has been granted in the previous configuration
intents = discord.Intents.default()
intents.message_content = True

class aclient(discord.Client):
  def __init__(self):
    super().__init__(intents = intents)
    self.added = False # added to make sure that the views will be synced only once

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.added:
      self.add_view(greet_view()) # add view to the Bot
      self.added = True
    print(f"Say hi to {self.user}!")

client = aclient()

# A view can hold up 25 buttons
class greet_view(discord.ui.View):
  def __init__(self) -> None:
      super().__init__(timeout=None)

  # First button
  @discord.ui.button(label='greet', custom_id = "greet_button", style = discord.ButtonStyle.blurple)
  async def greet_user(self, interaction: discord.Interaction, button: discord.ui.Button):
    user = interaction.user.id
    await interaction.response.send_message(f'Hello, <@{user}>, how are you doing today?')

  # You can add up to 25 buttons to the same view, but make sure it's custom_id and function name are always different!
  # Second button
  @discord.ui.button(label='say goodbye', custom_id = "good_bye_button", style = discord.ButtonStyle.red)
  async def say_goodbye_to_user(self, interaction: discord.Interaction, button: discord.ui.Button):
    user = interaction.user.id
    await interaction.response.send_message(f'Good bye, <@{user}>, hope to see you soon!')


@client.event
async def on_message(message):
  if message.content == 'Show Buttons':
    await message.channel.send(view=greet_view())
  return


# add the token of your bot
client.run('your-bot-token-here')