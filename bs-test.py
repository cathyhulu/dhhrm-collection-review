from bs4 import BeautifulSoup
import requests

url = 'https://dhhrm.catalogaccess.com/photos/4424'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

# soup.find_all('div', class_ = 'row')
soup.find('div', id_ = 'catalog-item-details-page-layout')

print(soup)