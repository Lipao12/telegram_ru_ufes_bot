import os
from dotenv import load_dotenv
from bot_repo import BotRepo
from menu_repo import Menu
from menu_controller import MenuController
from datetime import datetime

BASE_URL = "https://ru.ufes.br/cardapio"
DAY = f'/{datetime.today().strftime('%Y-%m-%d')}'

menu = Menu(BASE_URL)
infos = menu.get_day_menu(DAY)
menu_controller = MenuController(infos)
#print(menu_controller.show_menu())

load_dotenv()
BOT_TOKEN = os.getenv('TELEGRAM_API')

bot_repo = BotRepo(BOT_TOKEN, menu_controller)
bot_repo.register_handlers()
bot_repo.run()
