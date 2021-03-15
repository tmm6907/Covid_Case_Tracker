#main.py
from bs4 import BeautifulSoup
from county_trackers.models import Tracker
from background_task import background

import requests
import time
import re

@background
def covidpg():

    def starter_tag(string):
        return string and re.compile('Allegany').search(string)

    def end_tag(string):
        return string and not re.compile('Data not available').search(string)

    #Retrieve html file from webpage and initialize soup object on that file
    html_file = requests.get('https://www.wbaltv.com/article/covid-19-numbers-maryland-map-graphs-faq-february-22-28/35586153#').text
    soup = BeautifulSoup(html_file,'lxml')

    #Scrape page for county and print out results
    region = soup.find('div', class_='article-content--body-text')
    start = region.find('p', string = starter_tag)
    
    
    while(end_tag(start.string)): #isolates list of counties from rest of document
        string = start.string
        string = re.split('\w+', string)
        print(string)
        if re.match('[A-Z]', string[1]):
            countyname = (string[0]) + ' ' + (start[1])
            cases = start[2]
            deaths = start[3]
            probdeaths = start[4]
        else:
            countyname = string[0]
            cases = start[1]
            deaths = start[2]
            probdeaths = start[3]
        
        tracker = Tracker.objects.create_tracker(countyname, cases, deaths, probdeaths)
        tracker.save()


        #logging data into a folder of files that increment every day
        #nl = '\n' #new line character
        #logger = open(f'logs/log{index}.txt', 'a')
        #logger.write(f'Spilts: {temp_print}{nl}')
        #logger.write(f'The statistics for {countyname} county are:{nl}')
        #logger.write(f'Cases: {cases}{nl}')
        #logger.write(f'Deaths: {deaths}{nl}')
        #logger.write(f'Probable Deaths: {probdeaths}{nl}')
        #logger.close()
        
        start = start.next_sibling

    #print timestamp
    localt = time.localtime()
    print(f"Function Executed {localt}...")

        
