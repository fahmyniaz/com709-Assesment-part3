import csv


def searchByRank():
    rank=str(input('Enter the required Top rank'))
    csv_file=csv.reader(open('data/charts.csv','r'))

    for row in csv_file:
        if rank in row[5]:
            print(row)

print('Enter 1 to search by Artist Top Rank')

src=int(input('Enter here: '))

if src==1:
    searchByRank()
else:
    print('Sorry invalid input')
