# pcost.py
#
# Exercise 1.27

#def portfolio_cost(filename):
#    total_cost = 0.0
#    with open(filename, 'rt') as f:
#        headers = next(f)
#        for line in f:
#            row = line.split(',')
#            try:
#                total_cost = total_cost + float(row[1]) * float(row[2])
#            except:
#                print(f'Parse error in line {line}')
#    return total_cost
#
#
#cost = portfolio_cost('Data/portfolio.csv')
#print(f'Total cost is: {cost:0,.2f}')

import csv
import sys
def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                total_cost = total_cost + float(row[1]) * float(row[2])
            except:
                print(f'Parse error in line {row}')
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost is: {cost:0,.2f}')
 
