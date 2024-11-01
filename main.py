from menu_repo import Menu
from menu_controller import MenuController

BASE_URL = "https://ru.ufes.br/cardapio"
DAY = "/2024-11-01"

menu = Menu(BASE_URL)
infos = menu.get_day_menu(DAY)
menu_controller = MenuController(infos)
print(menu_controller.show_menu())

