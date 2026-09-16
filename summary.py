import csv

with open("server.csv", "r") as file:
    reader = csv.DictReader(file)

    or row in reader:
        print(row)