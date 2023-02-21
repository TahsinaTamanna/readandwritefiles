import csv

rows = []

infile = open("customers.csv", "r")
csvfile = csv.reader(infile)

outfile = open("customer_country1.csv", "w")

searchname = input("Please enter the name: ")

next(csvfile)  # skip the first line which is the header

outfile.write("Full Name, Country\n")

foundFlag = False

for record in csvfile:

    # outfile.write(record[1] + " " + record[2] + "," + record[4] + "\n")
    # outfile.write(fullname + "," + country + "\n")

    if record[1].lower() == searchname.lower():
        print("match found")
        print()
        print(f"First Name: {record[1]}")
        print(f"Last Name: {record[2]}")
        print(f"City: {record[3]}")
        print(f"Country: {record[4]}")
        print(f"Phone: {record[5]}")
        foundFlag = True


if not foundFlag:
    print("match not found")
