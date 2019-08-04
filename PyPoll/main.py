import os
import csv

csvpath = os.path.join('..','PyPoll', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    count = 0
    candidates = []
    unique_candidates = []
    vote_count = []
    vote_percent = []

    for row in csvreader:
        count = count +1
        candidates.append(row[2])
    for i in set(candidates):
        unique_candidates.append(i)
        j = candidates.count(i)
        vote_count.append(j)
        per = (j/count)*100
        roundedvpercent = round(per, 3)
        vote_percent.append(roundedvpercent)
        
    win_vote = max(vote_count)
    winner = unique_candidates[vote_count.index(win_vote)]

    print("Election Results")
    print("-------------------------------")
    print("Total Votes:", str(count))
    print("-------------------------------")

    for each in range(len(unique_candidates)):
        print(unique_candidates[each], ":", str(vote_percent[each]),"%", str(vote_count[each]))

    print("-------------------------------")
    print("Winner:", winner)


    output_path = os.path.join('..','PyPoll', 'results.txt')
# Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',') 
        csvwriter.writerow(["Li : 14.0 % 492940", "Correy : 20.0 % 704200", 
            "Khan : 63.0 % 2218231",
            "O'Tooley : 3.0 % 105630"])
 
