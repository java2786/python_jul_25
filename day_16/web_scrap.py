import requests
from bs4 import BeautifulSoup

url = "https://www.python.org"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

elements = soup.find_all("h1")
for e in elements:
    print(e.get_text())