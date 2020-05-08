# covid19
Web Scraper tracking US COVID19 statistics

For python 3, also requires Beautiful Soup python module

This app scrapes three pieces of data from worldometer.com:  US COVID19 cases, deaths, and recoveries.  It adds a timestamp
to each one, prints it to the terminal, and writes each entry to log.txt, deliminated with semi-colons.  A simple tkinter 
design lists each statistic and has a refresh button to update it, along with the current timestamp.  The app also adds each 
new entry to a list in order to plot graphs or other data science uses.

cases.py, deaths.py, and recovered.py are not currently used; the main file covid19.py contains all of them.  
I had thought about splitting the code across separate python scripts but couldn't get it to update the tkinter labels
properly. Will probably change to this model eventually.

To Do:
add graphing script using matplotlib
