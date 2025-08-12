import discord
from discord.ext import commands
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

TOKEN = os.getenv("DISCORD_TOKEN")
PORT = int(os.getenv("PORT", 10000))

# ---- Flask API ----
app = Flask(__name__)
CORS(app)

@app.route("/order", methods=["POST"])
def order():
    data = request.json
    pseudo = data.get("pseudo")
    product = data.get("product")
    details = data.get("details")

    if not pseudo or not product or not details:
        return jsonify({"error": "Missing fields"}), 400

    channel = bot.get_channel(CHANNEL_ID)  # Remplace CHANNEL_ID par ton ID de salon Discord
    if channel:
        message = f"📦 Nouvelle commande\n👤 {pseudo}\n🛒 {product}\n📝 {details}"
        bot.loop.create_task(channel.send(message))

    return jsonify({"status": "Order sent"}), 200

# ---- Bot Discord ----
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

# ---- Lancer Flask + Bot ----
import threading

def run_flask():
    app.run(host="0.0.0.0", port=PORT)

threading.Thread(target=run_flask).start()

bot.run(TOKEN)
