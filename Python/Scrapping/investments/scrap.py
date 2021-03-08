from requests import get
from bs4 import BeautifulSoup

req = get('https://www.infomoney.com.br/cotacoes/petrobras-petr4/')

content = ""
if req.status_code == 200:
    print('Requisição bem sucedida...')
    content = req.content

soup = BeautifulSoup(content, 'html.parser')

valor = ""
for div in soup.find_all('div', class_="value"):
    valor = (div.find('p').get_text())

porcentagem = ""
for div in soup.find_all('div', class_="percentage"):
    porcentagem = (div.find('p').get_text().strip())

print("PETR4 = R$", valor, porcentagem)
