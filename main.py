#main.py
import requests
from bs4 import BeautifulSoup

with open('mdcovid.mhtml', 'r') as html_file:
    soup = BeautifulSoup(html_file,'lxml')
    counties = soup.find_all('div')
    #for county in counties:
    #    countyname = county.find('p').text
    #    print(countyname, '/n')
    print(counties)