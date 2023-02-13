import csv

customer_totals = {}

with open("./sales.csv", "r") as sales_file:
    reader_sales = csv.reader(sales_file)
    # skipping the first line in the csv file as it contains a header record
    # in this file it would be "CustomerID, OrderDate,ShipDate,SubTotal,TaxAmt,Freight"
    next(sales_file)

    with open("./salesreport1.csv", "w", newline="") as sales_file_new1:
        writer_sales = csv.writer(sales_file_new1)
        writer_sales.writerow(["Customer ID", "Total"])

        for column in reader_sales:

            total = float(column[5]) + float(column[4]) + float(column[3])

            customer_id = column[0]

            if customer_id in customer_totals:
                customer_totals[customer_id] += total
            else:
                customer_totals[customer_id] = total

        for customer_id, total in customer_totals.items():
            writer_sales.writerow([customer_id, round(total, 2)])

sales_file.close()
sales_file_new1.close()

"""
            writer_sales.writerow(
                (
                    column[0],
                    round(float(column[5]) + float(column[4]) + float(column[3]), 2),
                )
            )
"""
