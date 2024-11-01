class MenuController:
    def __init__(self, meal) -> None:
        self.meal = meal

    def show_menu(self):
        message = ""
        for category, items in self.meal["meal"].items():
            emoji = self.get_emoji(category)
            message += f"{emoji} *{category}*:\n"
            for item in items:
                message += f"  - {item}\n"
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
