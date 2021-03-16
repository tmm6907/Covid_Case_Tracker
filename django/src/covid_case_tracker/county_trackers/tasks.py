#main.py
from django.shortcuts import render
from django.http import JsonResponse
from bs4 import BeautifulSoup
from background_task import background


from county_trackers import models

import requests
import time
import re
import logging

@background
def covidpg():
    def starter_tag(string):
        return string and re.compile('Allegany').search(string)

    def end_tag(string):
        return string and not re.compile('Data not available').search(string)

    #Retrieve html file from webpage and initialize soup object on that file
    html_file = requests.get(
        'https://www.wbaltv.com/article/covid-19-numbers-maryland-map-graphs-faq-february-22-28/35586153#').text
    soup = BeautifulSoup(html_file,'lxml')

    #Scrape page for county and print out results
    region = soup.find('div', class_='article-content--body-text')
    start = region.find('p', string = starter_tag)
    
    while(end_tag(start.string)): #isolates list of counties from rest of document
        string = start.string
        string = re.split("[ *()']+",string)
        #print(string)
        if re.match('[A-Z]', string[1]):
            if re.match('s', string[2]):
                countyname = string[0] + ' ' + string[1] + "'" + string[2]
                cases = string[3]
                deaths = string[4]
                probdeaths = string[5]
            else:
                countyname = string[0] + ' ' + string[1]
                cases = string[2]
                deaths = string[3]
                probdeaths = string[4]
        else:
            countyname = string[0]
            cases = string[1]
            deaths = string[2]
            probdeaths = string[3]
        
        tracker = models.Tracker.objects.create(title = countyname,cases = cases, deaths = deaths, prob_deaths = probdeaths)
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

