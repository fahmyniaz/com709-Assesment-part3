import csv

file_path = "data/charts.csv"

records = []

print("Loading data...", end="")

try:
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)

        for line in csv_reader:
            records.append(line)

    print("Done!")
    print(f"Successfully loaded {len(records)} records.")

    print("""

  Please select one of the following options:
   
    [1] Retrieve the details for the top ranked song for a particular day
	[2]Retrieve the details of the artist with the most top ranked songs
	[3]Retrieve the details of the 10 songs with the longest number of weeks on the board
	[4]Retrieve the song that has moved the most in ranking on the board
	[5]Visualise the top songs (the criteria for ‘top’ is up to you)


  """)

    selected_option = int(input())
    print(f"You have selected option: {selected_option}")

except IOError:
    print("Could not read the file.")
