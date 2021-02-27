#main.py
from bs4 import BeautifulSoup
import requests
import time

def covidpg():
    #keeps track of log number

    #Retrieve html file from webpage and initialize soup object on that file
    html_file = requests.get('https://www.wbaltv.com/article/covid-19-numbers-maryland-map-graphs-faq-february-22-28/35586153#').text
    soup = BeautifulSoup(html_file,'lxml')

    #Scrape page for county and print out results
    region = soup.find('div', class_='article-content--body-text')
    elements = region.find_all('p')
    for element in enumerate(elements):
        if 'Prince' in element.text: #for now I can only do PG county until I discover more about how to isolate tags that lack a tag identifier
            countyname = (element.text.split()[0]) + (element.text.split()[1])
            cases = element.text.split()[2]
            deaths = element.text.split()[3]
            probdeaths = element.text.split()[4]
            
            with open(f'logs/log.txt', 'a') as log:
                log.write(f'The statistics for {countyname} are: ')
                log.write(f'Cases: {cases}')
                log.write(f'Deaths: {deaths}')
                log.write(f'Probable Deaths: {probdeaths}')
            localt = time.localtime()
            print(f"File Saved {localt}...")

        