import requests
from bs4 import BeautifulSoup as bs
from .models import Product

URL_TEMPLATE = f"https://eda.ru/recepty/ingredienty/{Product.eda_id}"


def parse(url=URL_TEMPLATE):
    result_list = []
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    recipes = soup.find_all('div', class_='css-etyz2y')
    for recipe in recipes:
        link = 'https://eda.ru' + \
            recipe.find('a', class_='css-17vxl0k').get('href')
        name = recipe.find(
            'span', class_='css-x3ykye-Info').text
        prep_time = recipe.find(
            'span', class_='css-1re6mm4-Info').text
        result_dict = dict(link=link, name=name, prep_time=prep_time)
        result_list.append(result_dict)
    return result_list
