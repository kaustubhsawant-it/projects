import requests
from bs4 import BeautifulSoup


url = "http://127.0.0.1:5500/Python/Major/Web%20Scraper/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')

quotes = soup.find_all('div',class_='quote')

for quote in quotes:
    text = quote.find('span',class_='text').get_text()
    author = quote.find('small',class_='author').get_text()
    print(f"{text} - {author}")