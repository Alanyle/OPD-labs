from bs4 import BeautifulSoup as BS # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import urllib3
urllib3.disable_warnings()

def parse():
    g=1
    while True:
        page = requests.get('https://omgtu.ru/news/?PAGEN_1='+str(g), verify=False) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
        print(page.status_code) # смотрим ответ
        #html = BS(page.content, "html.parser")
        soup = BS(page.text, "html.parser") # передаем страницу в bs4
        block = soup.findAll('div', class_="news-card__content") # находим  контейнер с нужным классом
        description = ''
        date = ''
        if (len(block)):
            print('page = ' + str(g))
            for data in block: # проходим циклом по содержимому контейнера
                if data.find('h3'): # находим тег <p>
                    description = data.text # записываем в переменную содержание тега
                if description!='':
                    text = description[:11] + description[45:-36]
                    print(text)
                    with open("test.txt", "a", encoding="utf-8") as file:
                        file.write(text)
            g+=1
        else:
            break
if __name__ == '__main__':
    parse()