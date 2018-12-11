import csv
import os
total_net_amount = 0

csv_path = "../../../../Desktop/UDEN201811DATA3/Week3/HW/Instructions/PyBank/Resources/budget_data.csv"
with open (csv_path,"r") as f:
    reader = csv.reader(f)
    next(reader)
    val = []
    for row in reader:
        total_net_amount += int(row[1])
        total_months = reader.line_num - 1
        val.append(int(row[1]))
        if int(row[1]) == max(val):
            date = row[0]
        if int(row[1]) == min(val):
            date2 = row[0]
    print(f"Total Months:",total_months)
    print(f"Total:",total_net_amount)
    
    change_between_months = [x[1] - x[0] for x in list(zip(val,val[1:]))]
    Average = sum(change_between_months)/len(change_between_months)
    print(f"Average  Change:",round(Average,2))
    
    print("Greatest Increase in Profits:", date, max(val))
    print("Greatest Increase in losses:", date2, min(val))

