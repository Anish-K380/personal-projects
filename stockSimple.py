from datetime import date, timedelta
from collections import deque
import matplotlib.pyplot as graph

class Stock:
    def __init__(self, name = None, ISIN = None):
        if name is not None:
            self.name = name
            self.isin = ISIN
            self.load()
            return
        self.name = input('Enter ticker of stock:')
        self.company = input('Enter company of stock:')
        self.isin = input('Enter ISIN code of stock:')
        if self.isin in isins:
            print('Stock already exists')
            return
        isins.add(self.isin)
        self.startDate = date.today()
        self.endDate = date.today()
        self.prices = deque((0,))
        with open(path + 'stockList.txt', 'a') as file:
            file.write(self.name + f' {self.isin}\n')
        self.save()

    def details(self):
        print('ticker :', self.name)
        print('company :', self.company)
        print('ISIN :', self.isin)
        for i in range(max(0, len(self.prices) - 10), len(self.prices)):
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
            file.write(''.join((self.company, '\n', self.startDate.strftime('%d.%m.%Y'), '\n', self.endDate.strftime('%d.%m.%Y'))))
            for i in range(len(self.prices)):
                file.write('\n' + str(self.prices[i]))

    def load(self):
        with open(''.join((path, 'stock', self.isin, '.txt')), 'r') as file:
            self.company = line(file.readline())
            self.startDate = convert(line(file.readline()))
            self.endDate = convert(line(file.readline()))
            self.prices = deque()
            for i in range((self.endDate - self.startDate).days + 1):
                self.prices.append(float(line(file.readline())))

    def visualize(self, start = None, end = None):
        if start is None:
            start = self.startDate
        else:
            start = convert(start)
        if end is None:
            end = self.endDate
        else:
            end = convert(end)
        if start > end:
            print('The dates are reversed.')
            return
        if start < self.startDate:
            print('The starting date is out of range')
            return
        if end > self.endDate:
            print('The ending date is out of range.')
            return
        index = (start - self.startDate).days
        length = (end - start).days + 1
        dates = list()
        for i in range(length):
            dates.append(start + timedelta(days = i))
        graph.plot(dates, tuple(self.prices)[index: index + length], marker = 'o', label = f'{start} - {end}')
        graph.title(self.name)
        graph.xlabel('Date')
        graph.ylabel('Stock price')
        graph.xticks(rotation = 45)
        graph.show()

def loadOptions():
    for i in range(len(store)):
        print(f'{i + 1} - {store[i + 1][1]} - {store[i + 1][0]}')

def load(*serials):
    stocks = list()
    for i in serials:
        stocks.append(Stock(store[i][0], store[i][1]))
    if len(stocks) == 1:return stocks[0]
    return stocks

def convert(_date):
    day, month, year = tuple(map(int, _date.split('.')))
    return date(year, month, day)

dateInput = lambda message : convert(input(message))

line = lambda k : k.rstrip('\n')

path = ''

isins = set()

store = dict()
with open(path + 'stockList.txt', 'r') as file:
    serial = 1
    while True:
        info = file.readline()
        if not info:
            break
        name, isin = line(info).split()
        isins.add(isin)
        store[serial] = (name, isin)
        serial += 1
loadOptions()
