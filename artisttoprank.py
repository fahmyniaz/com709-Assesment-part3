import csv

with open ('data/charts.csv') as csvfile:
    reader = csv.reader(csvfile)

    count= 0
    fsa = []

    for row in reader:
        count = count = 0
        print(row)
        if count > 100:
            break