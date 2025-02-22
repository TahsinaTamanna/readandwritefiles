import csv

# opening the csv file in read mode
employeepay = open("EmployeePay.csv", "r")

# using the csv library, creating a csv object
# the delimiter ',' tells the program how the columns are seperated
employeepay_file = csv.reader(employeepay, delimiter=",")

# skipping the first line in the csv file as it contains a header record
# in this file it would be "ID,EmpFName,EmpLName,Salary, Bonus"
next(employeepay_file)


for record in employeepay_file:
    # this print statement shows that the variable record is a list
    # each element in the list corresponds to each column in the file

    print("Employee ID:", record[0])
    print("Name:", record[1] + " " + record[2])
    print(
        "Total Pay: $", round(float(record[3]) + float(record[3]) * float(record[4]), 2)
    )
    print("Calculated Bonus: $", round(float(record[3]) * float(record[4]), 2))

    input()

employeepay.close()
