import csv

def searchByDate():
    date=str(input('Enter the date\n'))
    csv_file=csv.reader(open('data/charts.csv','r'))

    for row in csv_file:
        if date==row[0]:
            print(row)

def searchByRank():
    rank=str(input('Enter the required rank'))
    csv_file=csv.reader(open('data/charts.csv','r'))

    for row in csv_file:
        if rank in row[1]:
            print(row)

print('Enter 1 to search by Date')
print('Enter 2 to search by Rank')

src=int(input('Enter here: '))

if src==1:
    searchByDate()
elif src==2:
    searchByRank()
else:
    print('Sorry invalid input')
