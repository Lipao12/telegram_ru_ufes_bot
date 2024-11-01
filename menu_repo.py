import urllib.request
from bs4 import BeautifulSoup

class Menu:
    def __init__(self, BASE_URL) -> None:
        self.base_url = BASE_URL

    def get_day_menu(self, day):
        fp = urllib.request.urlopen(self.base_url+day)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()

        soup = BeautifulSoup(mystr, 'html.parser')

        div_content = soup.find('div', class_='field-content')
        p_elements_string = []
        strong_elements_string = []

        if div_content:
            #print(div_content.prettify())
            p_elements = div_content.find_all('p')
            for p in p_elements:
                p_elements_string.append(p.text)

            strong_elements = div_content.find_all('strong')
            for strong in strong_elements:
                strong_elements_string.append(strong.text)

        else:
            print("Elemento não encontrado")

        strong_elements_string.append("end")

        excess_items = ['\xa0', '* Cardápio sujeito a alterações.', '** Informamos que todas as nossas preparações podem conter traços de glúten e leite (contaminação cruzada).']

        j = 1
        refeicao = {}
        for i in range(len(strong_elements_string) - 1):
            current_category = strong_elements_string[i]
            next_category = strong_elements_string[i + 1]
            refeicao[current_category] = []

            while j < len(p_elements_string) and p_elements_string[j] != next_category:
                if p_elements_string[j] not in excess_items:
                    refeicao[current_category].append(p_elements_string[j])
                j += 1
            j += 1

        extra_items = [item for item in p_elements_string if item in excess_items]

        print("Refecções categorizadas:")
        print(refeicao)

        print("\nItens extras:")
        print(extra_items)