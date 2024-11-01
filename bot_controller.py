import telebot

class BotController:
    def __init__(self, api, bot_repo) -> None:
        self.bot = telebot.TeleBot(api)
        self.bot_repo = bot_repo
        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            welcome_text = (
                "👋 Olá, seja bem-vindo ao *Bot do Cardápio RU da UFES*! \n\n"
                "📆 Eu estou aqui para te ajudar a consultar o cardápio de hoje e dos próximos dias no Restaurante Universitário da UFES.\n\n"
                "🔎 Aqui estão alguns comandos para você começar:\n"
                "  - /almoco: Veja o cardápio do almoço de hoje\n"
                "  - /jantar: Veja o cardápio do jantar de hoje\n"
                "  - /amanha: Receba o cardápio de amanhã\n"
                "  - /semana: Exibe o cardápio da semana\n\n"
                "📲 Basta escolher um comando para começar! Caso precise de ajuda, digite /help."
            )
            self.bot.reply_to(message, welcome_text, parse_mode="Markdown")
    
    def register_handlers(self):
        @self.bot.message_handler(commands=['almoco'])
        def send_lunch_menu(message):
            almoco_menu = self.bot_repo.get_today_lunch()
            self.bot.reply_to(message, almoco_menu, parse_mode="Markdown")

        @self.bot.message_handler(commands=['jantar'])
        def send_dinner_menu(message):
            jantar_menu = self.bot_repo.get_today_dinner()
            self.bot.reply_to(message, jantar_menu, parse_mode="Markdown")

    def run(self):
        print("Bot runnin...")
        self.bot.infinity_polling()
