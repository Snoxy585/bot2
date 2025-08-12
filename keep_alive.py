from flask import Flask, request, jsonify
from flask_cors import CORS
from threading import Thread
import asyncio

# On crée l'app Flask
app = Flask(__name__)
CORS(app)

# Variables globales (on va injecter bot et OWNER_ID depuis bot.py)
bot_instance = None
owner_id = None

@app.route("/")
def home():
    return "Bot API en ligne ✅"

@app.route("/order", methods=["POST"])
def receive_order():
    data = request.json
    pseudo = data.get("pseudo")
    product = data.get("product")
    details = data.get("details")

    async def send_dm():
        try:
            user = await bot_instance.fetch_user(owner_id)
            await user.send(
                f"📦 Nouvelle commande reçue !\n"
                f"**Client :** {pseudo}\n"
                f"**Produit :** {product}\n"
                f"**Détails :** {details}"
            )
            print(f"Commande envoyée à {user}")
        except Exception as e:
            print(f"Erreur envoi DM : {e}")

    asyncio.run_coroutine_threadsafe(send_dm(), bot_instance.loop)

    return jsonify({"status": "Commande envoyée en DM"}), 200

def run():
    port = 5000
    app.run(host="0.0.0.0", port=port)

def keep_alive(bot, owner):
    global bot_instance, owner_id
    bot_instance = bot
    owner_id = owner
    t = Thread(target=run)
    t.start()
