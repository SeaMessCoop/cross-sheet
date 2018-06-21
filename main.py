import csv
import inspect

def lineno(): #  Function that returns line number in program
    return inspect.currentframe().f_back.f_lineno

filepath = 'SeattleTo-priceSet.csv'
with open(filepath) as csvfile:
    rows = csv.reader(csvfile)
    rows = list(rows)
    header = rows[0]
    output_rows = [header]
    print(lineno(), '\nRows:', rows,
          lineno(), '\nHeader:', header,
          lineno(), '\noutput_rows:', output_rows)
    for (rowi, row) in enumerate(rows):
        output_row = []
        print(lineno(), 'Rows:', rowi, row)
        for (coli, col) in enumerate(header):
            print(lineno(), 'Columns:', coli, col)
            price1 = row[0]
            price2 = header[coli]

            if (price1 is '' or price2 is ''):
                output_row += ','
                continue

            price1 = float(price1)
            price2 = float(price2)

            min_price = min(price1, price2)
            max_price = max(price1, price2)
            total = round(max_price + .75 * min_price)
            print(lineno(), 'Min:', min_price, 'Max:', max_price, 'Total:', total)
            output_row.append(total)
        output_rows.append(output_row)
    with open('outputX.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(output_rows)
