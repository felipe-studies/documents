import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.quintoandar.com.br/')

content = ""
if req.status_code == 200:
    print('Requisição bem sucedida...')
    content = req.content

soup = BeautifulSoup(content, 'html.parser')
print(soup.get_text())

# https://medium.com/data-hackers/como-fazer-web-scraping-em-python-23c9d465a37f
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

def zapimoveis():
    from urllib.request import Request, urlopen
    # url_home = "https://www.zapimoveis.com.br/%(acao)s/%(tipo)s/%(localization)s/?pagina=%(page)s"
    url = "https://www.zapimoveis.com.br/"
    USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    request = Request(url)
    request.add_header('User-Agent', USER_AGENT)
    response = urlopen(request)
    print(response.status)