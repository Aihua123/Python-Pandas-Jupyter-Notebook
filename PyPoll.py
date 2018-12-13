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

    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------")
    # print(list(set(candidate_list)))
    # print(summary)

    x = 0
    for key,value in summary.items():
        pct_of_won = value/total_votes
        pct_of_won_formatted = "{:.3%}".format(pct_of_won)
        print(f"{key}: {pct_of_won_formatted} ({value})")
        if pct_of_won > x:
           x = pct_of_won
           winner = key
    print("------------------------")
    print(f"winner:{winner}")       
    





