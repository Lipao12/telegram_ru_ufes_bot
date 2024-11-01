from menu_repo import Menu

BASE_URL = "https://ru.ufes.br/cardapio"
DAY = "/2024-11-01"


menu = Menu(BASE_URL)
menu.get_day_menu(DAY)
