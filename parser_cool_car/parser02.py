import requests
from bs4 import BeautifulSoup
import csv

CSV = 'cars.csv'
URl = 'https://www.olx.ua/uk/transport/legkovye-avtomobili/'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


# print(get_html(URl))

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('tr', {'class': 'wrap'})
    result = []

    for link in links:
        result.append(
            {
                'address': link.find('small', {'class': 'breadcrumb x-normal'}).get_text(strip=True),
                'link': link.find('a',
                                  {'class': 'marginright5 link linkWithHash detailsLink linkWithHashPromoted'}).get(
                    'href'),
                'photo': link.find('img', {'class': 'fleft'}).get('src'),
                'cost': link.find('t1', {'class': 'price'}).get_text(strip=True),
                'number': link.find('a', {
                    'class': 'marginright5 link linkWithHash detailsLink linkWithHashPromoted'}).get_text(strip=True)

            }
        )

        return result


def save_doc(links, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            ['Название автомобиля', 'Ссылка на страницу продукта', 'Ссылка на фото машины', 'Стоимость машины',
             'Марка автомобиля'])
        for link in links:
            writer.writerow([link['number'], link['link'], link['photo'], link['cost'], link['address']])


def parser():
    REG = input('Сколько строк вы хотите спарсить: ')
    REG = int(REG.strip())
    html = get_html(URl)
    if html.status_code == 200:
        cars = []
        for page in range(1, REG + 1):
            print(f'Парсим страницу: {page}')
            html = get_html(URl, params={'page': page})
            cars.extend(get_content(html.text))
            save_doc(cars, CSV)

    else:
        print('ERROR')


parser()
