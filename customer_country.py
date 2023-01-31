import csv

# using the csv library
# opening the csv file in read mode
with open("./customers.csv", "r") as customer_file:
    reader_file = csv.reader(customer_file)
    # skipping the first line in the csv file as it contains a header record
    # in this file it would be "ID,FirstName,LastName,City,Country,Phone"
    next(customer_file)

    # opening the csv file in write mode
    with open("./customer_country.csv", "w", newline="") as customer_file_new:
        writer_file = csv.writer(customer_file_new)
        writer_file.writerow(["Full Name", "Country"])  # naming the headers
        for column in reader_file:
            writer_file.writerow(
                (column[1] + " " + column[2], column[4])
            )  # merging 2 columns for Full name

customer_file.close()
customer_file_new.close()
