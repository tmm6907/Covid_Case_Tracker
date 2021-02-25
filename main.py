#main.py

from bs4 import BeautifulSoup

with open('mdcovid.mhtml', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())
