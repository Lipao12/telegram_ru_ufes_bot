from datetime import datetime, timedelta

class MenuController:
    def __init__(self, menu_repo) -> None:
        self.menu_repo = menu_repo
    
    def get_menu_for_today(self, meal_type=None):
        day = f'/{datetime.today().strftime("%Y-%m-%d")}'
        try:
            info = self.menu_repo.get_day_menu(day)
            if not info:  
                return '🚫 Não há Cardápio para hoje.\n'
            return self.show_menu(info, meal_type)
        except Exception as e:
            return f'Ocorreu um erro ao obter o cardápio de hoje: {e}'
    
    def get_menu_for_tomorrow(self):
        tomorrow = datetime.today() + timedelta(days=1)
        day = f'/{tomorrow.strftime("%Y-%m-%d")}'
        try:
            info = self.menu_repo.get_day_menu(day)
            if not info:  
                return f'🚫 Não há Cardápio para o dia *{tomorrow.strftime("%d/%m/%Y")}*.'
            return self.show_menu(info)
        except Exception as e:
            return f'Ocorreu um erro ao obter o cardápio de amanhã: {e}'

    def show_menu(self, meals,meal_type=None):
        message = ""
        if meal_type and meal_type not in meals:
            return f"🚫 Não há *{meal_type}* disponível para o dia de hoje.\n"
        
        meals_to_show = {meal_type: meals[meal_type]} if meal_type in meals else meals

        for meal, categories in meals_to_show.items():
            message += f"🍴 *{meal}*\n\n"
            for category, items in categories.items():
                emoji = self.get_emoji(category)
                message += f"{emoji} *{category}*:\n"
                for item in items:
                    message += f"  - {item}\n"
                message += "\n"
            message += "\n"
        return message

    def get_emoji(self, category):
        emojis = {
            'Salada': '🥗',
            'Prato Principal': '🍽️',
            'Opção': '🍲',
            'Acompanhamento': '🍚',
            'Guarnição': '🍛',
            'Sobremesa': '🍍'
        }
        return emojis.get(category, '')
