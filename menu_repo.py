import urllib.request
from bs4 import BeautifulSoup

class Menu:
    def __init__(self, BASE_URL) -> None:
        self.base_url = BASE_URL

    def get_day_menu(self, day):
        fp = urllib.request.urlopen(self.base_url + day)
        mystr = fp.read().decode("utf8")
        fp.close()

        soup = BeautifulSoup(mystr, 'html.parser')
        menus = {}
        meal_sections = soup.find_all('div', class_='views-field')

        for i in range(0, len(meal_sections) - 1, 2):
            title_div = meal_sections[i].find('span', class_='field-content')
            body_div = meal_sections[i + 1].find('div', class_='field-content')

            if title_div and body_div:
                refeicao_nome = title_div.text.split(" - ")[0].strip()
                p_elements = [p.text for p in body_div.find_all('p')]
                strong_elements = [strong.text for strong in body_div.find_all('strong')]
                strong_elements.append("end")

                excess_items = [
                    '\xa0', '* Cardápio sujeito a alterações.',
                    '** Informamos que todas as nossas preparações podem conter traços de glúten e leite (contaminação cruzada).'
                ]

                j = 1
                meal = {}
                for k in range(len(strong_elements) - 1):
                    current_category = strong_elements[k]
                    next_category = strong_elements[k + 1]
                    meal[current_category] = []

                    while j < len(p_elements) and p_elements[j] != next_category:
                        if p_elements[j] not in excess_items:
                            meal[current_category].append(p_elements[j])
                        j += 1
                    j += 1

                menus[refeicao_nome] = meal

        return menus
