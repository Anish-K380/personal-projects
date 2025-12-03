from datetime import date, timedelta
from collections import deque

class Stock:
    def __init__(self, ISIN = None):
        if ISIN != None:
            self.isin = ISIN
            self.load()
            return
        self.name = input('Enter ticker of stock:')
        self.company = input('Enter company of stock:')
        self.isin = input('Enter ISIN code of stock:')
        self.startDate = date.today()
        self.endDate = date.today()
        self.prices = deque((0,))
        with open(path + 'stockList.txt', 'a') as file:
            file.write(self.isin)
        self.save()

    def details(self):
        print('ticker :', self.name)
        print('company :', self.company)
        print('ISIN :', self.isin)
        for i in range(len(self.prices)):
            print((self.startDate + timedelta(days = i)).strftime('%d.%m.%Y :'), self.prices[i])

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
        if difference >= len(self.prices):
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

    def save(self):
        with open(''.join((path, 'stock', self.isin, '.txt')), 'w') as file:
            file.write(''.join((self.name, '\n', self.company, '\n', self.startDate.strftime('%d.%m.%Y'), '\n', self.endDate.strftime('%d.%m.%Y'))))
            for i in range(len(self.prices)):
                file.write('\n' + str(self.prices[i]))

    def load(self):
        with open(''.join((path, 'stock', self.isin, '.txt')), 'r') as file:
            self.name = line(file.readline())
            self.company = line(file.readline())
            day, month, year = tuple(map(int, line(file.readline()).split('.')))
            self.startDate = date(year, month, day)
            day, month, year = tuple(map(int, line(file.readline()).split('.')))
            self.endDate = date(year, month, day)
            self.prices = deque()
            for i in range((self.endDate - self.startDate).days + 1):
                self.prices.append(float(line(file.readline())))
    
def dateInput(message):
    year, month, day = tuple(map(int, input(message).split('.')))
    return date(day, month, year)

line = lambda k : k.rstrip('\n')

path = '/home/anish/pyFile/stockSimple/'
