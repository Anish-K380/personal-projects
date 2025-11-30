import csv
from datetime import date, timedelta
from collections import deque

class Stock:
    def __init__(self):
        self.name = input('Enter ticker of stock:')
        self.company = input('Enter company of stock:')
        self.startDate = date.today()
        self.endDate = date.today()
        self.prices = deque((0,))

    def changeStartDate(self, newDate = None):
        if newDate is None:
            newDate = dateInput('Enter date in format (dd.mm.yyyy):')
        if newDate > self.endDate:
            self.startDate = newDate
            self.endDate = newDate
            self.prices = deque((0,))
        difference = (newDate - self.startDate).days
        default = self.prices[0]
        if difference >= len(self.prices):
            self.endDate = newDate
            self.prices = deque((0,))
            difference = 0
        while difference > 0:
            self.prices.popleft()
            difference -= 1
        while difference < 0:
            self.prices.appendleft(default)
            difference += 1
        self.startDate = newDate

    def changeEndDate(self, newDate = None):
        if newDate is None:
            newDate = dateInput('Enter date in format (dd.mm.yyyy):')
        if newDate < self.startDate:
            self.startDate = newDate
            self.endDate = newDate
            self.prices = deque((0,))
        difference = (self.endDate - newDate).days
        default = self.prices[-1]
        if difference >= len(prices):
            self.startDate = newDate
            self.prices = deque((0,))
            difference = 0
        while difference > 0:
            self.prices.pop()
            difference -= 1
        while difference < 0:
            self.prices.append(default)
            difference += 1
        self.endDate = newDate

    def stockPriceEdit(self):
        dateStart = dateInput('Enter start range of date in format (dd.mm.yyyy):')
        dateEnd = dateInput('Enter end range of date in format (dd.mm.yyyy):')
        if dateStart > dateEnd:
            print('Just to inform you, you switched the dates around. I can handle it though.')
            dateStart, dateEnd = dateEnd, dateStart
        if dateStart < self.startDate:
            self.changeStartDate(dateStart)
        if dateEnd > self.endDate:
            self.changeEndDate(dateEnd)
        print('Enter prices corresponding with date')
        for i in range((dateStart - self.startDate).days, (dateEnd - self.startDate).days + 1):
            self.prices[i] = float(input((self.startDate + timedelta(days = i)).strftime('%d.%m.%Y :')))
    
def dateInput(message):
    dateTuple = tuple(map(int, input(message).split('.')))
    return date(dateTuple[2], dateTuple[1], dateTuple[0])
