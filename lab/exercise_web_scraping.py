import csv
from time import sleep

from bs4 import BeautifulSoup
import requests


class HouseScraper:
    def __init__(self, initial_url, encoding_type='windows-1251'):
        self.initial_url = initial_url
        self.encoding_type = encoding_type
        self.initial_response = requests.get(self.initial_url)
        self.initial_response = self.encode_response(self.initial_response)
        self.number_of_pages = self.get_number_of_pages()

        self.cycle_through_pages_and_get_the_info()

    def encode_response(self, response):
        response.encoding = self.encoding_type
        return response

    @staticmethod
    def get_current_soup(response):
        current_soup = BeautifulSoup(response.text, 'html.parser')
        return current_soup

    def get_number_of_pages(self):
        result = self.get_current_soup(self.initial_response).find(
            'span',
            class_='pageNumbersInfo',
        )
        pages = result.text.split(' ')[-1]
        return int(pages)

    @staticmethod
    def sleep_for_a_while():
        sleep(0.1)

    @staticmethod
    def clear_csv_file_and_create_th():
        with open('listings.csv', 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Location', 'Price', 'Photo'])

    def cycle_through_pages_and_get_the_info(self):
        try:
            self.clear_csv_file_and_create_th()

            for page in range(1, self.number_of_pages + 1):
                current_url = self.initial_url[:-1] + str(page)
                current_response = requests.get(current_url)
                current_response = self.encode_response(current_response)
                current_soup = self.get_current_soup(current_response)

                houses_photos = current_soup.find_all(
                    'a',
                    class_='photoLink',
                )

                houses_tables = current_soup.find_all(
                    'td',
                    valign='top',
                    width='270',
                    height='40',
                )

                for i in range(len(houses_tables)):
                    price = houses_tables[i].find('div', class_='price').text
                    location = houses_tables[i].find('a', class_='lnk2').text
                    photo = houses_photos[i + 2].find('img')['src']

                    print(f"{location} - {price}\n{photo}")
                    print()

                    with open('listings.csv', 'a', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        writer.writerow([location, price, photo])

                self.sleep_for_a_while()

            print('Done!')

        except Exception as e:
            print(e)


new_scraping = HouseScraper(
    'https://www.imot.bg/pcgi/imot.cgi?act=3&slink=9a33mn&f1=1',
)
