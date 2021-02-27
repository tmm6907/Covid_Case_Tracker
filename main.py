#main.py
from bs4 import BeautifulSoup
import requests


def covidpg(index):
    index+=1 #keeps track of log number

    #Retrieve html file from webpage and initialize soup object on that file
    html_file = requests.get('https://www.wbaltv.com/article/covid-19-numbers-maryland-map-graphs-faq-february-22-28/35586153#').text
    soup = BeautifulSoup(html_file,'lxml')

    #Scrape page for county and print out results
    region = soup.find('div', class_='article-content--body-text')
    elements = region.find_all('p')
    for element in elements:
        if 'Prince' in element.text:
            countyfname = element.text.split()[0]
            countylname = element.text.split()[1]
            cases = element.text.split()[2]
            deaths = element.text.split()[3]
            probdeaths = element.text.split()[4]
            
            log = open(f"log{index}.txt", "w") # not working for some reason
            log.write(f"The statistics for {countyfname} {countylname} are: ")
            log.write(f"Cases: {cases}")
            log.write(f"Deaths: {deaths}")
            log.write(f"Probable Deaths: {probdeaths}")

        