import discord
import re
import os
from dotenv import load_dotenv
from discord.ext import commands
#from googletrans import Translator

#translator = Translator()

# Intents setup (for reading messages)
intents = discord.Intents.default()
intents.messages = True  # Ensure the bot can read messages
intents.message_content = True  # Required for accessing message content
intents.guilds = True
intents.members = True
intents.voice_states = True

load_dotenv()

#ot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="/", intents=intents)
token = os.getenv('BOT_TOKEN')
APPROVED_URLS = ["https://www.curseforge.com", "https://modrinth.com"]
TARGET_CHANNEL_NAME = 'mod-recommendation'
url_pattern = re.compile(r"https://(?:www\.)?(curseforge\.com|modrinth\.com)")


@bot.event
async def on_ready():
    print(f'Bot has logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    # Corrected method name to add_roles()
    role = discord.utils.get(member.guild.roles, name="monkey")

    if role:
        try:
            await member.add_roles(role)  # Correct method
            print(f"Assigned monkey role to {member.name}.")
        except discord.Forbidden:
            print(f"Permission error: Cannot assign roles to {member.name}.")
        except discord.HTTPException as e:
            print(f"An error occurred: {e}")
    else:
        print("Role 'monkey' not found!")


@bot.event
async def on_message(message):
    # Ignore bot's own messages
    if message.author == bot.user:
        return
    
    else:
    
        #sent_text = message.content
        # detection = translator.detect(sent_text)
        # detected_language = detection.lang

        # if detected_language == 'tl':
        #     if str(message.channel) == 'general':
        #         try:
        #             translated_text = translator.translate(sent_text, dest='en').text
        #             await message.channel.send(
        #                 f"Detected language: {detected_language}\n"
        #                 f"Original: {sent_text}\n"
        #                 f"Translated: {translated_text}"
        #             )
        #         except Exception as e:
        #             pass

        if message.author.id == <userid>:
            try:
                await message.delete()
                print(f'Deleted message from {message.author}: {message.content}')
            except discord.errors.Forbidden:
                print("Bot has no permission to delete message")


        if str(message.channel) == TARGET_CHANNEL_NAME:
        # Check if message contains approved URLs
            if not url_pattern.search(message.content):
                try:
                    await message.delete()
                    print(f'Deleted message from {message.author}: {message.content}')
                except discord.errors.Forbidden:
                    print("Bot has no permission to delete message")


# Start the bot
bot.run(token)
