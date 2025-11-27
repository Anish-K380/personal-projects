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
        pass

a = date.today()
a.day = 16
print(a.day)
