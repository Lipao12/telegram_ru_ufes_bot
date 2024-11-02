import telebot
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')

class BotController:
    def __init__(self, api, bot_repo) -> None:
        self.bot = telebot.TeleBot(api)
        self.bot_repo = bot_repo
        @self.bot.message_handler(commands=['start', 'olá', 'oi'])
        def send_welcome(message):
            welcome_text = (
                "👋 Olá, seja bem-vindo ao *Bot do Cardápio RU da UFES*! \n\n"
                "📆 Eu estou aqui para te ajudar a consultar o cardápio de hoje e dos próximos dias no Restaurante Universitário da UFES.\n\n"
                "🔎 Aqui estão alguns comandos para você começar:\n"
                "  - /almoco: Veja o cardápio do almoço de hoje\n"
                "  - /jantar: Veja o cardápio do jantar de hoje\n"
                "  - /amanha: Receba o cardápio de amanhã\n\n"
                "📲 Basta escolher um comando para começar!"
            )
            self.bot.reply_to(message, welcome_text, parse_mode="Markdown")
    
    def register_handlers(self):
        @self.bot.message_handler(commands=['almoco'])
        def send_lunch_menu(message):
            day = f'_{datetime.today().strftime("%d/%m/%Y - %A")}_\n'
            almoco_menu = day + "\n" + self.bot_repo.get_today_lunch()
            encouragement_message = (
                                    "\n🌟 Espero que aproveite sua refeição! Se precisar de mais informações, "
                                    "não hesite em usar os comandos:\n"
                                    "  - /jantar: Para ver o cardápio do jantar\n"
                                    "  - /amanha: Para saber o cardápio de amanhã\n"
                                    "  - /start: Para ver as opções disponíveis."
                                )
            self.bot.reply_to(message, almoco_menu+encouragement_message, parse_mode="Markdown")

        @self.bot.message_handler(commands=['jantar'])
        def send_dinner_menu(message):
            day = f'_{datetime.today().strftime("%d/%m/%Y - %A")}_\n'
            jantar_menu = day + "\n" + self.bot_repo.get_today_dinner()
            encouragement_message = (
                                    "\n🌟 Espero que aproveite sua refeição! Se precisar de mais informações, "
                                    "não hesite em usar os comandos:\n"
                                    "  - /almoco: Para ver o cardápio do almoço de hoje\n"
                                    "  - /amanha: Para saber o cardápio de amanhã\n"
                                    "  - /start: Para ver as opções disponíveis."
                                )            
            self.bot.reply_to(message, jantar_menu+encouragement_message, parse_mode="Markdown")

        @self.bot.message_handler(commands=['amanha'])
        def send_tomorrow_menu(message):
            encouragement_message = (
                                    "\n🌟 Espero que aproveite sua refeição! Se precisar de mais informações, "
                                    "não hesite em usar os comandos:\n"
                                    "  - /almoco: Para ver o cardápio do almoço de hoje\n"
                                    "  - /jantar: Para ver o cardápio do jantar\n"
                                    "  - /start: Para ver as opções disponíveis."
                                ) 
            tomorrow_menu = self.bot_repo.get_tomorrow_menu()
            self.bot.reply_to(message, tomorrow_menu+ "\n\n" +encouragement_message, parse_mode="Markdown")

    def run(self):
        print("Bot running...")
        self.bot.infinity_polling()
