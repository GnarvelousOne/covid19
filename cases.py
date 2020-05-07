#!/usr/bin/env/ python

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import datetime

global  uscasesreport

def getcases():
    uscasesreport = ''

    webpage_response = requests.get('https://www.worldometers.info/coronavirus/country/us/')
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    covid_div = soup.find_all(class_ = 'maincounter-number')

    timenow = str(datetime.datetime.now().strftime("%a, %b %d %I:%M:%S %p"))

    divlist = []
    for i in covid_div:
        divlist.append(i)

    uscasesdirty = list(divlist[0])

    uscases = str(uscasesdirty[1]).replace('<span style="color:#aaa">', '').replace(' </span>', '')

    uscasesreport = timenow + ': U.S. COVID-19 cases: ' + uscases

    print(uscasesreport)
    return uscasesreport

#getcases()
