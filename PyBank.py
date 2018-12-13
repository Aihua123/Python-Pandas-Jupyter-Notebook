import csv
import os
total_net_amount = 0

csv_path = "../../../../Desktop/UDEN201811DATA3/Week3/HW/Instructions/PyBank/Resources/budget_data.csv"
with open (csv_path,"r") as f:
    reader = csv.reader(f)
    next(reader)
    val = []
    date = []
    for row in reader:
        total_net_amount += int(row[1])
        total_months = reader.line_num - 1
        val.append(int(row[1]))
        date.append(row[0])
    

    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_net_amount}")
    
    change_between_months = [x[1] - x[0] for x in list(zip(val,val[1:]))]
    Average = sum(change_between_months)/len(change_between_months)
    max_change = max(change_between_months)
    min_change = min(change_between_months)
    date_max = change_between_months.index(max(change_between_months))
    date_min = change_between_months.index(min(change_between_months))
    print(f"Average  Change: ${round(Average,2)}")
    
    print(f"Greatest Increase in Profits: {date[date_max + 1]} ${max_change}")
    print(f"Greatest Increase in losses: {date[date_min + 1]} ${min_change}")

