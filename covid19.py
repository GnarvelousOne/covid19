#!/usr/bin/env/ python

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import time
import datetime
from matplotlib import pyplot as plt
try:
    from Tkinter import *
    import tkFont
except ImportError:
    from tkinter import *
    from tkinter import font as tkFont

global c,d,r,uscasesreport,usdeathsreport,usrecoveredreport

master = Tk()
master.title("U.S. COVID-19 Tracker")

webpage_response = requests.get('https://www.worldometers.info/coronavirus/country/us/')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
covid_div = soup.find_all(class_ = 'maincounter-number')

timenow = str(datetime.datetime.now().strftime("%a, %b %d %I:%M:%S %p"))

divlist = []
for i in covid_div:
    divlist.append(i)

uscasesdirty = list(divlist[0])
usdeathsdirty = list(divlist[1])
usrecovereddirty = list(divlist[2])

uscases = str(uscasesdirty[1]).replace('<span style="color:#aaa">', '').replace(' </span>', '')
usdeaths = str(usdeathsdirty[1]).replace('<span>', '').replace('</span>', '')
usrecovered = str(usrecovereddirty[1]).replace('<span>', '').replace('</span>', '')

uscasesreport = timenow + ': U.S. COVID-19 cases: ' + uscases
usdeathsreport = timenow + ': U.S. COVID-19 deaths: ' + usdeaths
usrecoveredreport = timenow + ': U.S. COVID-19 recoveries: ' + usrecovered

print(uscasesreport)
print(usdeathsreport)
print(usrecoveredreport)

with open('log.txt', 'a') as reportLog:
    reportLog.write(uscasesreport+';\n')
    reportLog.write(usdeathsreport+';\n')
    reportLog.write(usrecoveredreport+';\n')
reportLog.close()

x_cases = []
x_deaths = []
x_recovered = []

x_cases.append(uscases)
x_deaths.append(usdeaths)
x_recovered.append(usrecovered)

#plt.plot(range(len(x_cases)), x_cases)
#plt.show()

screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
button_width = 10
button_height = 5
button_border = 3
button_font = tkFont.Font(family='latin modern typewriter variable width', size=14)
button_text_color = "#d1e0e0"
button_bg_color = "#537979"
bg_color = '#d1e0e0'
label_height = 5
label_width = 60
label_font = tkFont.Font(family='latin modern typewriter variable width', size=14)
#label_background = "#f0f5f5"
label_border = 3
label_relief = RAISED

c = StringVar()
d = StringVar()
r = StringVar()

c.set(str(uscasesreport))
d.set(str(usdeathsreport))
r.set(str(usrecoveredreport))

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

    c.set(str(uscasesreport))
    print(uscasesreport)

    with open('log.txt', 'a') as reportLog:
        reportLog.write(uscasesreport+';\n')
    reportLog.close()

    x_cases.append(uscases)

    return uscasesreport

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

    d.set(str(usdeathsreport))
    print(usdeathsreport)

    with open('log.txt', 'a') as reportLog:
        reportLog.write(usdeathsreport+';\n')
    reportLog.close()

    x_deaths.append(usdeaths)

    return usdeathsreport

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

    r.set(str(usrecoveredreport))
    print(usrecoveredreport)

    with open('log.txt', 'a') as reportLog:
        reportLog.write(usrecoveredreport+';\n')
    reportLog.close()

    x_recovered.append(usrecovered)

    return usrecoveredreport

caseslabel = Label(master, bg=bg_color, bd=label_border,
relief=label_relief, width=label_width, height=label_height, font=label_font, textvariable=c)
caseslabel.grid(column=1, row=1, columnspan=2, sticky= W+E+N+S)

deathslabel = Label(master, bg=bg_color, bd=label_border,
relief=label_relief, width=label_width, height=label_height, font=label_font, textvariable=d)
deathslabel.grid(column=1, row=2, columnspan=2, sticky= W+E+N+S)

recoveredlabel = Label(master, bg=bg_color, bd=label_border,
relief=label_relief, width=label_width, height=label_height, font=label_font, textvariable=r)
recoveredlabel.grid(column=1, row=3, columnspan=2, sticky= W+E+N+S)

casesbutton = Button(master, text="Refresh", command=getcases, fg=button_text_color, bg=button_bg_color,
width=button_width, height=button_height, bd=button_border, font=button_font)
casesbutton.grid(column=3, row=1)

deathsbutton = Button(master, text='Refresh', command=getdeaths, fg=button_text_color, bg=button_bg_color,
width=button_width, height=button_height, bd=button_border, font=button_font)
deathsbutton.grid(column=3, row=2)

recoveredbutton = Button(master, text='Refresh', command=getrecovered, fg=button_text_color, bg=button_bg_color,
width=button_width, height=button_height, bd=button_border, font=button_font)
recoveredbutton.grid(column=3, row=3)

mainloop()
