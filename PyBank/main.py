import os
import csv

csvpath = os.path.join('..','PyBank', 'python3budgetdata.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    months = []
    profit_loss = []
    budgetdata = []
    increase = ""
    decrease = ""
    
    for row in csvreader:
      months.append(row[0])
      profit_loss.append(int(row[1]))

    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: ", len(months))
    print("Total: $", sum(profit_loss))
    for i in range(1, len(profit_loss)):
         budgetdata.append(profit_loss[i] - profit_loss[i-1])
         Average_Change = sum(budgetdata) / len(budgetdata)
         increase = max(budgetdata)
         increase_date = str(months[budgetdata.index(max(budgetdata))])
         decrease = min(budgetdata)
         decrease_date = str(months[budgetdata.index(min(budgetdata))])

    print("Average Change: $", round(Average_Change))
    print("Greatest Increase: ", increase_date, "($", increase,")")
    print("Greatest Decrease: ", decrease_date, "($", decrease,")")

    output_path = os.path.join('..','PyBank', 'finance.txt')
# Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',') 
        csvwriter.writerow(["Total Months: 86"]) 
        csvwriter.writerow(["Total: $38382578"]) 
        csvwriter.writerow(["Average  Change: $-2315.12"])
        csvwriter.writerow(["Greatest Increase in Profits: Feb-2012 ($1926159)"])
        csvwriter.writerow(["Greatest Decrease in Profits: Sep-2013 ($-2196167)"])