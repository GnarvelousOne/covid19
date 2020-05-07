#!/usr/bin/env/ python

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import datetime

global usrecoveredreport

def getrecovered():
    usrecoveredreport = ''

    webpage_response = requests.get('https://www.worldometers.info/coronavirus/country/us/')
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    covid_div = soup.find_all(class_ = 'maincounter-number')

    timenow = str(datetime.datetime.now().strftime("%a, %b %d %I:%M:%S %p"))

    divlist = []
    for i in covid_div:
        divlist.append(i)

    usrecovereddirty = list(divlist[2])

    usrecovered = str(usrecovereddirty[1]).replace('<span>', '').replace('</span>', '')

    usrecoveredreport = timenow + ': U.S. COVID-19 recoveries: ' + usrecovered

    print(usrecoveredreport)

    return usrecoveredreport

#getrecovered()
