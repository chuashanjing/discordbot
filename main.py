import discord
import re

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)
token = '<bot token>'
APPROVED_URLS = ["https://www.curseforge.com", "https://modrinth.com"]
TARGET_CHANNEL_NAME = 'mod-recommendation'
url_pattern = re.compile(r"https://(?:www\.)?(curseforge\.com|modrinth\.com)")

@client.event
async def on_ready():
    print(f'Bot has logged in as {client.user}')

@client.event
async def on_member_join(member):
    
    role = discord.utils.get(member.guild.roles, name="monkey")

    if role:
        try:
            await member.add_roles(role)
            print(f"Assigned 'friends' role to {member.name}.")
        except discord.Forbidden:
            print(f"Permission error: Cannot assign roles to {member.name}.")
        except discord.HTTPException as e:
            print(f"An error occurred: {e}")
    else:
        print("Role 'monkey' not found!")

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if str(message.channel) == TARGET_CHANNEL_NAME:
    
        if not url_pattern.search(message.content):
            try:
                await message.delete()
                print(f'Deleted message from {message.author}: {message.content}')
            except discord.errors.Forbidden:
                print("Bot has no permission to delete message")


client.run(token)
