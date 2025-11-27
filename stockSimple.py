import csv
from datetime import date
from collections import deque

class Stock:
    def __init__(self):
        self.name = input('Enter ticker of stock:')
        self.company = input('Enter company of stock:')
        self.startDate = date.today()
        self.prices = deque()

    def changeStartDate(self):
        newDate = dateInput('Enter date in format (dd.mm.yyyy):')
        difference = (newDate - self.startDate).days
        default = 0
        if len(self.prices) != 0:
            default = self.prices[0]
        while difference < 0:
            difference += 1
            self.prices.appendleft(default)
        if difference >= len(self.prices):
            difference = 0
            self.prices = deque()
        self.startDate = newDate

    def stockPriceEdit(self):
        dateStart = dateInput('Enter start range of date in format (dd.mm.yyyy):')
        dateEnd = dateInput('Enter end range of date in format (dd.mm.yyyy):')
        leftAdd = (self.startDate - dateStart).days
        while leftAdd > 0:
        print('Enter prices corresponding with date')
        for i in range((dateEnd - dateStart).days + 1):
            print
    
def dateInput(message):
    dateTuple = tuple(map(int, input(message).split('.')))
    return date(dateTuple[2], dateTuple[1], dateTuple[0])
