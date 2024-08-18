import csv

fname = input()
new_object = {}

with open(fname, 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        for index in range(len(row)):
            if row[index] not in new_object:
                new_object[row[index]] = row.count(row[index])

    for key,value in new_object.items():
        print(key,value)