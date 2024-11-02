import os
from dotenv import load_dotenv
from bot_controller import BotController
from bot_repo import BotRepo
from menu_repo import Menu
from menu_controller import MenuController

BASE_URL = "https://ru.ufes.br/cardapio"

load_dotenv()
BOT_TOKEN = os.getenv('TELEGRAM_API')

menu = Menu(BASE_URL)
menu_controller = MenuController(menu)
bot_repo = BotRepo(menu_controller)
bot_controller = BotController(BOT_TOKEN, bot_repo)
bot_controller.register_handlers()
bot_controller.run()
