#main.py
from bs4 import BeautifulSoup
import requests
import time

def covidpg(index):
    #keeps track of log number

    #Retrieve html file from webpage and initialize soup object on that file
    html_file = requests.get('https://www.wbaltv.com/article/covid-19-numbers-maryland-map-graphs-faq-february-22-28/35586153#').text
    soup = BeautifulSoup(html_file,'lxml')

    #Scrape page for county and print out results
    region = soup.find('div', class_='article-content--body-text')
    start = region.find('p', string='Allegany  6,409       (198)        1*')
    
    while('Data not available' not in start.text):
        if start.text.split()[1].isalpha():
            countyname = (start.text.split()[0]) + ' ' + (start.text.split()[1])
            cases = start.text.split()[2]
            deaths = start.text.split()[3]
            probdeaths = start.text.split()[-1]
        else:
            countyname = (start.text.split()[0])
            cases = start.text.split()[1]
            deaths = start.text.split()[2]
            probdeaths = start.text.split()[3]
        
        nl = '\n'
        logger = open(f'logs/log{index}.txt', 'a')
        logger.write(f'The statistics for {countyname} county are:{nl}')
        logger.write(f'Cases: {cases}{nl}')
        logger.write(f'Deaths: {deaths}{nl}')
        logger.write(f'Probable Deaths: {probdeaths}{nl}')
        
        start = start.next_sibling
localt = time.localtime()
print(f"File Saved {localt}...")

        