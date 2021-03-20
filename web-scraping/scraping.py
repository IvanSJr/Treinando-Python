import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/?tags=python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for p in html.select('.question-summary'):
    titulo = p.select_one('.question-hyperlink')
    print(f'Pergunta:{titulo.text}\n')

