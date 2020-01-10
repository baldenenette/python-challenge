import os
import csv

# Create the lists to store data. 
#Initialize the variables as required.
date = []
revenue = []
profit_change = []
monthly_change = []
total_revenue = 0

#greatestIncrease = ["", 0]
#greatestDecrease = ["", 99999999999]
#Open the CSV using the set path csvpath
csvpath = os.path.join("Resources","budget_data.csv")
pathout = os.path.join("Resources", "budget_analysis.txt")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    print ("Financial analysis")
    print ("------------------------")
    for row in csvreader:
        for row in csvreader:
           date.append(row[0])
           revenue.append(row[1])
    total_month = len(date)
    print("Total months: " + str(total_month))

    #print(total_revenue)
    #i=0 
    for i in range(len(revenue)):
        total_revenue += int(revenue[i])
    print("Total revenue: $" + str(total_revenue))
    #i=0
    for i in range(len(revenue) -1):
        profit = int(revenue[i+1]) - int(revenue[i])   
        monthly_change.append(profit)
    Total = sum(monthly_change)
    average_change = Total / len(monthly_change)
    print("Average change: $" + str(average_change))
    greatest_increase = max(monthly_change)
    y = monthly_change.index(greatest_increase)
    increase_date = date[y+1]
   
    
#Greatest Decrease
    greatest_decrease = min(monthly_change)
    x = monthly_change.index(greatest_decrease)
    print("Greatest increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")" )
    decrease_date = date[x+1]
    print("Greatest decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")" )
    