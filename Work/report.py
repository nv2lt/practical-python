# report.py
#
# Exercise 3.12

import csv
import fileparse
import stock
import tableformat
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename, 'rt') as filedata:
        portdicts = fileparse.parse_csv(filedata, select=['name','shares','price'], types=[str,int,float]) 
    portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename, 'rt') as filedata:
        pricelist = fileparse.parse_csv(filedata, has_headers=False, types=[str,float])
    return dict(pricelist)

def make_report_data(portfolio, prices):
    report = []
    for s in portfolio:
        report.append((s.name, s.shares, prices[s.name], prices[s.name] - s.price))
    return report
 
def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfilio and price data files
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    import sys
    if len(sys.argv) == 4:
        portfolio_filename = sys.argv[1]
        prices_filename = sys.argv[2]
        print_format = sys.argv[3]
    else:
        portfolio_filename = 'Data/portfolio.csv'
        prices_filename = 'Data/prices.csv'
        print_format = 'txt'

    portfolio_report(portfolio_filename, prices_filename, print_format)


if __name__ == '__main__':
    import sys
    main(sys.argv)


