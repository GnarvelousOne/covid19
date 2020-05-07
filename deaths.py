#!/usr/bin/env/ python

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import datetime

global usdeathsreport

def getdeaths():
    usdeathsreport = ''

    webpage_response = requests.get('https://www.worldometers.info/coronavirus/country/us/')
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    covid_div = soup.find_all(class_ = 'maincounter-number')

    timenow = str(datetime.datetime.now().strftime("%a, %b %d %I:%M:%S %p"))

    divlist = []
    for i in covid_div:
        divlist.append(i)

    usdeathsdirty = list(divlist[1])

    usdeaths = str(usdeathsdirty[1]).replace('<span>', '').replace('</span>', '')

    usdeathsreport = timenow + ': U.S. COVID-19 deaths: ' + usdeaths

    print(usdeathsreport)

    return usdeathsreport

#getdeaths()
