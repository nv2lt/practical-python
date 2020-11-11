# report.py
#
# Exercise 2.4

import sys
import csv
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                name = record['name']
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
            #holding = (row[0], int(row[1]), float(row[2]))
            #holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
            portfolio.append({'name': name, 'shares': nshares, 'price': price})
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        line_number = 0
        for row in rows:
            try:
                line_number += 1
                prices[row[0]] = float(row[1])
            except IndexError:
                #print(f'null value in row {line_number}. It was not added to result')
                pass
    return prices

def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        report.append((s['name'], s['shares'], prices[s['name']], prices[s['name']] - s['price']))
    return report
 
def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    hyphen = '-'
    dollar = '$'
    for i in headers:
        print('%10s' %i, end=" ")
    print()
    print(f'{hyphen*10:>10s} {hyphen*10:>10s} {hyphen*10:>10s} {hyphen*10:>10s}')
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {dollar+str(price):>10} {change:10.2f}')
 
#if len(sys.argv) == 2:
#    filename = sys.argv[1]
#else:
#    filename = 'Data/portfolio.csv'

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

#initial_cost = 0.0
#current_cost = 0.0
#
#for share_name in portfolio:
#    initial_cost += share_name['price'] * share_name['shares']
#    current_cost += prices[share_name['name']] * share_name['shares']
#
#print(f'Current Value of the portfolio is: {current_cost:0,.2f}')
#print(f'Initial Value of the portfolio was: {initial_cost:0,.2f}')
#print(f'Gain is: {(current_cost - initial_cost):0,.2f}')
#

#for r in report:
#    print('%10s %10d %10.2f %10.2f' %r)



