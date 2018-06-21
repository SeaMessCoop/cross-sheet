import csv

filepath = './data/SeattleTo-priceSet.csv'
with open(filepath) as csvfile:
    rows = csv.reader(csvfile)
    rows = list(rows)
    header = rows[0]
    output_rows = []
    for (irow, row) in enumerate(rows):
        output_row = []
        for (icol, col) in enumerate(header):
            price1 = row[0]
            price2 = header[icol]

            # prevent overwriting anything that's already been set
            if (row[icol]):
                print('value present', row[icol])
                output_row.append(row[icol])
                continue

            # if the row and column are the same we're
            # going to the same place so just put the
            # one base price.
            if (irow == icol):
                output_row.append(price1)
                continue

            # ignore anything that doesn't have a price set
            if (price1 is '' or price2 is ''):
                output_row.append('')
                continue

            price1 = float(price1)
            price2 = float(price2)

            min_price = min(price1, price2)
            max_price = max(price1, price2)
            total = round(max_price + .75 * min_price)
            output_row.append(total)
        output_rows.append(output_row)
    with open('output.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(output_rows)
