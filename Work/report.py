# report.py
#
# Exercise 3.12

import csv
import fileparse
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename, 'rt') as filedata:
        portfolio = fileparse.parse_csv(filedata, select=['name','shares','price'], types=[str,int,float]) 
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename, 'rt') as filedata:
        pricelist = fileparse.parse_csv(filedata, has_headers=False, types=[str,float])
    return dict(pricelist)

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
 

def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

def main(argv):
    import sys
    if len(sys.argv) == 3:
        portfolio_filename = sys.argv[1]
        prices_filename = sys.argv[2]
    else:
        portfolio_filename = 'Data/portfolio.csv'
        prices_filename = 'Data/prices.csv'

    portfolio_report(portfolio_filename, prices_filename)


if __name__ == '__main__':
    import sys
    main(sys.argv)


