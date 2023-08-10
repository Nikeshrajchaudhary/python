import requests
from bs4 import BeautifulSoup
url="https://schoolworkspro.com/"

r=requests.get(url)
print(r)
print(r.status_code)
print(r.url)
htmlcontent=(r.content)
print(htmlcontent)

soup=BeautifulSoup(htmlcontent, 'html.parser')

print(soup.prettify())
print(soup.title)