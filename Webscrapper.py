import requests
from bs4 import BeautifulSoup

base = 'https://www.falabella.com'
r = requests.get(base+'/falabella-cl/category/cat1320008/Ver-Todo-Moda-Hombre')
soup = BeautifulSoup(r.text, 'html.parser')
searchResults = soup.find(id='testId-searchResults-products')
divs = soup.div
for div in divs:
    print(div['id'])

