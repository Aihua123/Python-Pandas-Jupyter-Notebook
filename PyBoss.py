import csv
import os

csv_path = "../../../../Desktop/UDEN201811DATA3/Week3/HW/ExtraContent/Instructions/PyBoss/employee_data.csv"   

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(csv_path,"r")as f:
    reader = csv.reader(f)
    new_data =[]
    next(reader)
    for row in reader:
        emp_id,name,dob,ssn,state = row
        first_name = name.split()[0]
        last_name = name.split()[1]
        dob_formatted = dob.split("-")[1] + "/" + dob.split("-")[2] + "/" + dob.split("-")[0] 
        ssn_formatted = "***-**-" + ssn.split("-")[2]
        abbrev_state = us_state_abbrev.get(state)
        
        new_data.append([emp_id,first_name,last_name,dob_formatted,ssn_formatted,abbrev_state])
        
with open('new_employee_data.csv', 'w') as f:
    writer = csv.writer(f)
    for _row in new_data:
        writer.writerow(_row)
