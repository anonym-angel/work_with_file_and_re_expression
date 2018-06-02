import requests
import re


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













if __name__ == '__main__':
    regular_expression()