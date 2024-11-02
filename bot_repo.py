from datetime import datetime, timedelta
from menu_controller import MenuController
from menu_repo import Menu

BASE_URL = "https://ru.ufes.br/cardapio"

class BotRepo:
    def __init__(self, menu_controller) -> None:
        self.menu_controller = menu_controller
    
    def get_today_lunch(self):
        return self.menu_controller.get_menu_for_today("Almoço")
    
    def get_today_dinner(self):
        return self.menu_controller.get_menu_for_today("Jantar")
    
    def get_tomorrow_menu(self):
        tomorrow_menu = self.menu_controller.get_menu_for_tomorrow()
        return tomorrow_menu
        
    def get_next_week_menu(self):
        pass
    
