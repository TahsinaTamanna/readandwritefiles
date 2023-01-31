import csv

with open("./sales.csv", "r") as sales_file:
    reader_sales = csv.reader(sales_file)
    # skipping the first line in the csv file as it contains a header record
    # in this file it would be "CustomerID, OrderDate,ShipDate,SubTotal,TaxAmt,Freight"
    next(sales_file)

    with open("./salesreport.csv", "w", newline="") as sales_file_new:
        writer_sales = csv.writer(sales_file_new)
        writer_sales.writerow(["Customer ID", "Total"])
        for column in reader_sales:
            writer_sales.writerow(
                (
                    column[0],
                    "$",
                    +float(column[5]) + float(column[4]) + float(column[3]),
                )
            )

sales_file.close()
sales_file_new.close()
