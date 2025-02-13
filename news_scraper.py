import requests
from bs4 import BeautifulSoup

def fetch_market_news():
    """ Scrapes market news headlines from a financial website """
    url = "https://www.bloomberg.com/markets"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = [headline.text for headline in soup.find_all('h3')]
    return headlines
