import requests
from bs4 import BeautifulSoup


link = 'https://en.wikipedia.org/wiki/Fortune_500'
# target_class = 'wikitable sortable plainrowheaders jquery-tablesorter'
target_class = 'wikitable'


class CustomScraper:
    def __init__(self, url, target_object_class, encoding_type='windows-1251'):
        self.url = url
        self.target_class = target_object_class
        self.encoding_type = encoding_type
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }       # Without it, the server assumes it’s a bot and blocks you.

    def _encode_response(self, response):
        response.encoding = self.encoding_type
        return response

    def get_results(self):
        response = self._encode_response(requests.get(self.url, headers=self.headers))

        if response.status_code != 200:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return

        # here we would parse the response content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the target element by class name
        table = soup.find('table', {'class': self.target_class})
        if not table:
            print(f"No table found with class '{self.target_class}'")
            return

        # Extract and print all table rows
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all(['td', 'th'])
            cols = [col.get_text(strip=True) for col in cols]
            print(cols)


if __name__ == '__main__':
    new_scraping = CustomScraper(link, target_class)
    new_scraping.get_results()
