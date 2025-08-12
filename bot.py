import discord
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()

print("Lancement du bot...")

bot = discord.Client(intents=discord.Intents.all())
OWNER_ID = int(os.getenv("OWNER_ID"))

@bot.event
async def on_ready():
    print(f"✅ Bot allumé en tant que {bot.user}")

# Lancer le serveur Flask
keep_alive(bot, OWNER_ID)

# Lancer le bot Discord
bot.run(os.getenv("DISCORD_TOKEN"))
