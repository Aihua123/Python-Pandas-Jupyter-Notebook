import csv
import os

csv_path = "../../../../Desktop/UDEN201811DATA3/Week3/HW/Instructions/PyPoll/Resources/election_data.csv"
with open (csv_path,"r") as f:
    reader = csv.reader(f)
    next(reader)
    candidate_list = []
    summary = {}
    for row in reader:
        total_votes = reader.line_num - 1
        candidate_list.append(row[2])
        voter,county,candidate = row
        if candidate in summary:
            summary[candidate] += 1
        else:
            summary[candidate] = 1

    print(f"Total Votes:",total_votes)
    # print(list(set(candidate_list)))
    # print(summary)

    x = 0
    for key,value in summary.items():
        pct_of_won = value/total_votes
        print(key,"{:.2%}".format(pct_of_won),value)
        if pct_of_won > x:
           x = pct_of_won
           winner = key
    print(f"winner:",winner)       
    





