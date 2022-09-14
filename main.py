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

  [1]Retrieve the details for the top ranked song for a particular day
` [2]Retrieve the details of the artist with the most top ranked songs
  [3]Retrieve the details of the 10 songs with the longest number of weeks on the board
  [4]Retrieve the song that has moved the most in ranking on the board
  [5]Visualise the top songs (the criteria for ‘top’ is up to you)

  """)

    selected_option = int(input('Input a value: '))
    print(f"You have selected option: {selected_option}\n")

    if selected_option == 1:
        date = input('Enter Date: ')
        for record in records:
            if date == record[0] and 1 == int(record[1]):
                print(record[2])
                break

    elif selected_option == 2:
        # step 1 - Find top ranked songs and number of times they ranked number 1
        # Step 2 - Find maximum of number of times
        # Step 3 - Find the corresponding artist of the song
        artist_count = {}
        for record in records:
            if 1 == int(record[1]):
                if record[3] in artist_count.keys():
                    count = artist_count[record[3]] + 1
                    artist_count.update({record[3]: count})
                else:
                    artist_count[record[3]] = 1

        count_list = list(artist_count.values())
        count_list.sort(reverse=True)
        max = count_list[0]

        for artist in artist_count:
            if artist_count[artist] == max:
                print(artist)
                break


    elif selected_option == 3:
        def display_longest_no_weeks_songs():
            songs = {}
            for record in records:
                if record[2] not in songs:
                    songs[record[2]] = int(record[6])

            weeks = list(songs.values())
            unique_weeks = list(set(weeks))
            unique_weeks.sort(reverse=True)
            n = 1
            for week in unique_weeks:
                for song in songs:
                    if songs[song] == week:
                        if n == 10:
                            break
                        print(song)
                        n += 1
                if n == 10:
                    break

    elif selected_option == 4:
        songs_peak_rank = {}
        songs_lowest_rank = {}

        for record in records:
            song = record[2]
            p_rank = int(record[5])
            if song in songs_peak_rank:
                if p_rank > songs_peak_rank[song]:
                    songs_peak_rank.update({song: p_rank})
            else:
                songs_peak_rank[song] = p_rank

        for record in records:
            song = record[2]
            l_rank = int(record[5])
            if song in songs_lowest_rank:
                if l_rank < songs_lowest_rank[song]:
                    songs_lowest_rank.update({song: l_rank})
            else:
                songs_lowest_rank[song] = l_rank

        difference = 0
        moved_song = None
        for song in songs_peak_rank:
            temp_diff = songs_peak_rank[song] - songs_lowest_rank[song]
            if temp_diff > difference:
                difference = temp_diff
                moved_song = song
        print(moved_song)

except IOError:
    print("Could not read the file.")
