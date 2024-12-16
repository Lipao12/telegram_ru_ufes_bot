# main.py
import os
from dotenv import load_dotenv
from bot_controller import BotController
from bot_repo import BotRepo
from menu_repo import Menu
from menu_controller import MenuController
from flask import Flask

# Configurações do Flask
app = Flask(__name__)

BASE_URL = "https://ru.ufes.br/cardapio"

load_dotenv()
BOT_TOKEN = os.getenv('TELEGRAM_API')
print(f"BOT_TOKEN: '{BOT_TOKEN}'")
menu = Menu(BASE_URL)
menu_controller = MenuController(menu)
bot_repo = BotRepo(menu_controller)
bot_controller = BotController(BOT_TOKEN, bot_repo)
bot_controller.register_handlers()

@app.route('/')
def health_check():
    return "Bot is running!"

def run_bot():
    bot_controller.run()

if __name__ == '__main__':
    import threading
    
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
