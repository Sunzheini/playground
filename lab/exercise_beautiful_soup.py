import requests
from bs4 import BeautifulSoup


class CustomScraper:
    def __init__(self, url, encoding_type='windows-1251'):
        self.url = url
        self.encoding_type = encoding_type
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }       # Without it, the server assumes it’s a bot and blocks you.
        self.soup = None
        self.total_results = 0

    def _encode_response(self, response):
        response.encoding = self.encoding_type
        return response

    def get_results(self, appendix: str, type_of_element: str, identifier: str, identifier_value: str):
        complete_url = self.url + appendix
        response = self._encode_response(requests.get(complete_url, headers=self.headers))

        if response.status_code != 200:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return

        # here we would parse the response content with BeautifulSoup
        self.soup = BeautifulSoup(response.text, 'html.parser')
        if not self.soup:
            print("Soup object is not initialized. Please run get_results() first.")
            return

        if type_of_element == 'table':
            # Find the target element by class name
            table = self.soup.find('table', {identifier: identifier_value})
            if not table:
                print(f"No table found with {identifier} '{identifier_value}'")
                return

            # Extract and print all table rows
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all(['td', 'th'])
                cols = [col.get_text(strip=True) for col in cols]

                self.total_results += 1
                print(cols)


if __name__ == '__main__':
    link = 'https://en.wikipedia.org/wiki/Fortune_500'
    target_class = 'wikitable'

    new_scraping = CustomScraper(link, target_class)
    new_scraping.get_results('', 'table', 'class', target_class)
