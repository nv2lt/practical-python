# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(data, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if isinstance(data, str):
        print('Cannot import a string as data. Provide data that can be parsed by csv.reader')
        return None

    #with open(filename) as f:
    rows = csv.reader(data, delimiter=delimiter)

    # Read the file headers
    if has_headers:
        headers = next(rows)

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        if not has_headers:
            raise RuntimeError(f'select argument requires column headers')
        try:
            indices = [headers.index(colname) for colname in select]
        except RuntimeError as e:
            print(e)
        headers = select
    else:
        indices = []

    records = []
    for rownum, row in enumerate(rows):
        try:
            if not row:     # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices ]

            # Allow type conversions in each row
            if types:
                row = [func(val) for func, val in zip(types, row) ]

            # If filename has headers make a dictionary, else a list of tuples
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        except ValueError as e:
            if not silence_errors:
                if has_headers:
                    rownum +=1
                print(f'Row {rownum}: Couldn\'t convert {row}')
                print(f'Row {rownum}: {e}')
    return records
