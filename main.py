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
        print('\nСтраница номер {}'.format(count))

        def get_baskino():
            url = 'http://baskino.me/new/page/' + str(count)
            page = requests.get(url).text
            soup = BeautifulSoup(page, "html.parser")
            divs = soup.find_all('div', {'class': 'shortpost'})
            return divs

        def find_content():
            for div in get_baskino():
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


# -------------------------- Задание номер 3 --------------------------

def get_habr():
    url = 'https://habr.com/users/mkulesh/posts/'
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    heading = soup.find_all('a', {'class': 'post__title_link'})
    return heading


def get_find():
    print('Заголовки публикаций Михаила Кулеша имеют следующий вид:')
    [print(div.text) for div in get_habr()]


if __name__ == '__main__':
    print('Первое задание выполнено:')
    regular_expression()

    print('\nВторое задание выполнено:')
    cycle_parsing()

    print('\nТретье задание выполнено:')
    get_find()
