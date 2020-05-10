#!/usr/bin/env/ python

import requests
from bs4 import BeautifulSoup
#from time import sleep
from random import randint
import time
import datetime
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import font as tkFont
#from charts import *

global c,d,r,uscasesreport,usdeathsreport,usrecoveredreport, oldtimecases, oldtimedeaths, oldtimerecovered, ccounter, dcounter, rcounter

master = Tk()
master.title("U.S. COVID-19 Tracker")

webpage_response = requests.get('https://www.worldometers.info/coronavirus/country/us/')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
covid_div = soup.find_all(class_ = 'maincounter-number')

timenow = datetime.datetime.now()
oldtimecases = timenow
oldtimedeaths = timenow
oldtimerecovered = timenow
ccounter = 0
dcounter = 0
rcounter = 0

divlist = []
for i in covid_div:
    divlist.append(i)

uscasesdirty = list(divlist[0])
usdeathsdirty = list(divlist[1])
usrecovereddirty = list(divlist[2])

uscases = str(uscasesdirty[1]).replace('<span style="color:#aaa">', '').replace(' </span>', '')
usdeaths = str(usdeathsdirty[1]).replace('<span>', '').replace('</span>', '')
usrecovered = str(usrecovereddirty[1]).replace('<span>', '').replace('</span>', '')

uscasesreport = str(timenow.strftime("%a, %b %d %I:%M:%S %p")) + ': U.S. COVID-19 cases: ' + uscases
usdeathsreport = str(timenow.strftime("%a, %b %d %I:%M:%S %p")) + ': U.S. COVID-19 deaths: ' + usdeaths
usrecoveredreport = str(timenow.strftime("%a, %b %d %I:%M:%S %p")) + ': U.S. COVID-19 recoveries: ' + usrecovered

print(uscasesreport)
print(usdeathsreport)
print(usrecoveredreport)

with open('log.txt', 'a') as reportLog:
    reportLog.write(uscasesreport+';\n')
    reportLog.write(usdeathsreport+';\n')
    reportLog.write(usrecoveredreport+';\n')
reportLog.close()

y_cases = []
y_deaths = []
y_recovered = []

y_cases.append(uscases)
y_deaths.append(usdeaths)
y_recovered.append(usrecovered)

ccounter += 1
dcounter += 1
rcounter += 1

#plt.plot(range(len(y_cases)), y_cases)
#plt.show()


def getcases():
    global oldtimecases, ccounter
    uscasesreport = ''

    webpage_response = requests.get('https://www.worldometers.info/coronavirus/country/us/')
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    covid_div = soup.find_all(class_ = 'maincounter-number')

    timenow = datetime.datetime.now()
    diff = timenow - oldtimecases
    diff = '.'.join(str(diff).split('.')[:2])
    if ccounter > 1:
        oldtimecases = datetime.datetime.now()

    divlist = []
    for i in covid_div:
        divlist.append(i)

    uscasesdirty = list(divlist[0])

    uscases = str(uscasesdirty[1]).replace('<span style="color:#aaa">', '').replace(' </span>', '')

    uscasesreport = str(timenow.strftime("%a, %b %d %I:%M:%S %p")) + ': U.S. COVID-19 cases: ' + uscases
    timechange = "\n" + (str(diff[0]) + " hour(s), " + str(diff[2:4]) + " minute(s), and " + str(diff[5:7]) + " second(s) since last cases update.")

    c.set(str(uscasesreport) + timechange)
    print(uscasesreport + timechange)

    with open('log.txt', 'a') as reportLog:
        reportLog.write(uscasesreport+';\n')
    reportLog.close()

    y_cases.append(uscases)

    ccounter += 1

    return uscasesreport

def getdeaths():
    global oldtimedeaths, dcounter
    usdeathsreport = ''

    webpage_response = requests.get('https://www.worldometers.info/coronavirus/country/us/')
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    covid_div = soup.find_all(class_ = 'maincounter-number')

    timenow = datetime.datetime.now()
    diff = timenow - oldtimedeaths
    diff = '.'.join(str(diff).split('.')[:2])
    if dcounter > 1:
        oldtimedeaths = datetime.datetime.now()

    divlist = []
    for i in covid_div:
        divlist.append(i)

    usdeathsdirty = list(divlist[1])

    usdeaths = str(usdeathsdirty[1]).replace('<span>', '').replace('</span>', '')

    usdeathsreport = str(timenow.strftime("%a, %b %d %I:%M:%S %p")) + ': U.S. COVID-19 deaths: ' + usdeaths
    timechange = "\n" + (str(diff[0]) + " hour(s), " + str(diff[2:4]) + " minute(s), and " + str(diff[5:7]) + " second(s) since last deaths update.")

    d.set(str(usdeathsreport) + timechange)
    print(usdeathsreport + timechange)

    with open('log.txt', 'a') as reportLog:
        reportLog.write(usdeathsreport+';\n')
    reportLog.close()

    y_deaths.append(usdeaths)

    dcounter += 1

    return usdeathsreport

def getrecovered():
    global oldtimerecovered, rcounter
    usrecoveredreport = ''

    webpage_response = requests.get('https://www.worldometers.info/coronavirus/country/us/')
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, "html.parser")
    covid_div = soup.find_all(class_ = 'maincounter-number')

    timenow = datetime.datetime.now()
    diff = timenow - oldtimerecovered
    diff = '.'.join(str(diff).split('.')[:2])
    if rcounter > 1:
        oldtimerecovered = datetime.datetime.now()

    divlist = []
    for i in covid_div:
        divlist.append(i)

    usrecovereddirty = list(divlist[2])

    usrecovered = str(usrecovereddirty[1]).replace('<span>', '').replace('</span>', '')

    usrecoveredreport = str(timenow.strftime("%a, %b %d %I:%M:%S %p")) + ': U.S. COVID-19 recoveries: ' + usrecovered
    timechange = "\n" + (str(diff[0]) + " hour(s), " + str(diff[2:4]) + " minute(s), and " + str(diff[5:7]) + " second(s) since last recoveries update.")

    r.set(str(usrecoveredreport) + timechange)
    print(usrecoveredreport + timechange)

    with open('log.txt', 'a') as reportLog:
        reportLog.write(usrecoveredreport+';\n')
    reportLog.close()

    y_recovered.append(usrecovered)

    rcounter += 1

    return usrecoveredreport

def casesgraph():
    months = range(12)
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    #cases = [y_cases]

    #y_cases = covid19.y_cases

    plt.figure(figsize=(10,8))

    #y_lower = [i - (i*0.1) for i in y_cases]
    #y_upper = [i + (i*0.1) for i in y_cases]

    plt.plot(months, y_cases)
    #plt.fill_between(months, y_lower, y_upper, alpha=0.2)

    ax = plt.subplot()
    ax.set_xticks(months)
    ax.set_xticklabels(month_names)

    plt.show()

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
label_width = 65
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


caseslabel = Label(master, bg=bg_color, bd=label_border,
relief=label_relief, width=label_width, height=label_height, font=label_font, textvariable=c)
caseslabel.grid(column=1, row=1, columnspan=2, sticky= W+E+N+S)

deathslabel = Label(master, bg=bg_color, bd=label_border,
relief=label_relief, width=label_width, height=label_height, font=label_font, textvariable=d)
deathslabel.grid(column=1, row=2, columnspan=2, sticky= W+E+N+S)

recoveredlabel = Label(master, bg=bg_color, bd=label_border,
relief=label_relief, width=label_width, height=label_height, font=label_font, textvariable=r)
recoveredlabel.grid(column=1, row=3, columnspan=2, sticky= W+E+N+S)

casesbutton = Button(master, text="Update", command=getcases, fg=button_text_color, bg=button_bg_color,
width=button_width, height=button_height, bd=button_border, font=button_font)
casesbutton.grid(column=3, row=1)

deathsbutton = Button(master, text='Update', command=getdeaths, fg=button_text_color, bg=button_bg_color,
width=button_width, height=button_height, bd=button_border, font=button_font)
deathsbutton.grid(column=3, row=2)

recoveredbutton = Button(master, text='Update', command=getrecovered, fg=button_text_color, bg=button_bg_color,
width=button_width, height=button_height, bd=button_border, font=button_font)
recoveredbutton.grid(column=3, row=3)

chartbutton = Button(master, text='Get Charts', command="casesgraph", fg=button_text_color, bg=button_bg_color,
width=button_width, height=(button_height*3), bd=button_border, font=button_font)
chartbutton.grid(column=4, row=1, rowspan=3, sticky= W+E+N+S)

mainloop()
