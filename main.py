#main.py
import requests
from bs4 import BeautifulSoup

html_file = requests.get('https://www.wbaltv.com/article/covid-19-numbers-maryland-map-graphs-faq-february-22-28/35586153#').text

#with open('mdcovid.mhtml', 'r') as html_file:
soup = BeautifulSoup(html_file,'lxml')
soup.prettify()
region = soup.find('div', class_='article-content--body-text')
elements = region.find_all('p')
countyname= ''
for element in elements:
    if 'Prince' in element.text:
        countyfname = element.text.split()[0]
        countylname = element.text.split()[1]
        cases = element.text.split()[2]
        deaths = element.text.split()[3]
        probdeaths = element.text.split()[4]
        
        print(f"The statistics for {countyfname} {countylname} are:")
        print(f"Cases: {cases} ")
        print(f"Deaths: {deaths} ")
        print(f"Probable Deaths: {probdeaths} ")

