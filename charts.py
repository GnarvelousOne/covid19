#!/usr/bin/env/ python

from matplotlib import pyplot as plt
from covid19 import y_cases

def casesGraph():
    months = range(12)
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    #cases = [y_cases]

    #y_cases = covid19.y_cases

    plt.figure(figsize=(10,8))

    y_lower = [i - (i*0.1) for i in y_cases]
    y_upper = [i + (i*0.1) for i in y_cases]

    plt.plot(months, y_cases)
    plt.fill_between(months, y_lower, y_upper, alpha=0.2)

    ax = plt.subplot()
    ax.set_xticks(months)
    ax.set_xticklabels(month_names)

    plt.show()

casesGraph()
