import requests
import re
import shutil
from bs4 import BeautifulSoup

# -------------------------- Задание номер 1 --------------------------


def read_file(open_file='list_of_tourists.txt', mode='r'):
    with open(open_file, mode) as f:
        read_f = f.read()
        return read_f


def regular_expression():
    file = read_file()
    search_email = r'[\w]+@[\w.-]+'
    result = re.findall(search_email, file)
    [print(item) for item in result]
    print('Всего e-mail: {}'.format(len(result)))


# -------------------------- Задание номер 2 --------------------------

def cycle_parsing():
    count = 1
    while count <= 3:
        print('Страница номер {}'.format(count))

        def get_html():
            url = 'http://baskino.me/new/page/' + str(count)
            page = requests.get(url).text
            soup = BeautifulSoup(page, "html.parser")
            divs = soup.find_all('div',  {'class': 'shortpost'})
            return divs

        def find_content():
            for div in get_html():
                div_title = div.find('div', {'class': 'posttitle'})
                link_text = div_title.find('a').text
                print(link_text)

                img = div.find('div', {'class': 'postcover'})
                img_src = img.find('img').get('src')
                src = img_src
                response = requests.get(src, stream=True)
                with open('img/' + link_text + '.jpg', 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)

        find_content()
        count += 1


if __name__ == '__main__':
    print('Первое задание выполнено:')
    regular_expression()

    print('\nВторое задание выполнено:')
    cycle_parsing()