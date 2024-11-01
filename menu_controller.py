class MenuController:
    def __init__(self, meals) -> None:
        self.meals = meals

    def show_menu(self, meal_type=None):
        message = ""
        meals_to_show = {meal_type: self.meals[meal_type]} if meal_type in self.meals else self.meals

        for meal, categories in meals_to_show.items():
            message += f"*{meal}*\n\n"
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
