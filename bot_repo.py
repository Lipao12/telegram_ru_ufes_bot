import telebot

class BotController:
    def __init__(self, menu_controller) -> None:
        self.menu_controller = menu_controller
    
    def get_today_lunch(self):
        return self.menu_controller.show_menu("Almoço")
    
    def get_today_dinner(self):
        return self.menu_controller.show_menu("Jantar")
    
    def get_tomorrow_menu(self):
        pass
    
    def get_next_week_menu(self):
        pass
    
