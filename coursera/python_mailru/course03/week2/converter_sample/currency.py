from bs4 import BeautifulSoup
from decimal import Decimal
import requests


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}')
    soup = BeautifulSoup(response.content, 'xml')
    cur_from_value, cur_from_nominal, cur_to_value, cur_to_nominal = 0, 0, 0, 0
    try:
        cur_from_value = float(
            str(soup.find('CharCode', text=cur_from).find_next_sibling('Value').string).replace(',', '.'))
        cur_from_nominal = float(soup.find('CharCode', text=cur_from).find_next_sibling('Nominal').string)
    except AttributeError:
        pass
    try:
        cur_to_value = float(
            str(soup.find('CharCode', text=cur_to).find_next_sibling('Value').string).replace(',', '.'))
        cur_to_nominal = float(soup.find('CharCode', text=cur_to).find_next_sibling('Nominal').string)
    except AttributeError:
        pass

    if cur_to == 'RUR' and cur_from == 'RUR':
        result = amount
    elif cur_from == 'RUR':
        result = amount / (cur_to_value * cur_to_nominal)
    elif cur_to == 'RUR':
        result = amount * cur_from_value / cur_from_nominal
    else:
        result = (amount * cur_from_value / cur_from_nominal) / (cur_to_value * cur_to_nominal)
    result = Decimal(result).quantize(Decimal("1.0000"))
    return result
