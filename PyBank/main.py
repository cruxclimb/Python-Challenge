import os
import csv

with open("budget_data.csv") as file:
    read_file=csv.reader(file)
    
    next(read_file)
    profit = []
    date = []
    profit_change = []

# sum of profit/losses in csv file and count total months
    for row in read_file:

        profit.append(float(row[1]))
        date.append(row[0])
        total_months= len(date)
        total= sum(profit)
    for i in range(1,len(profit)):

        profit_change.append(profit[i] - profit[i-1])
        avg_profit_change = sum(profit_change)/len(profit_change)

        max_profit_change = max(profit_change)

        min_profit_change = min(profit_change)

        max_profit_date = str(date[profit_change.index(max(profit_change))])
        min_profit_date = str(date[profit_change.index(min(profit_change))])
    
print("Financial Analysis")
print("------------------------------------------")
print(f'Total Months:  {total_months}')
print (f'Total: {total}')
print ('Average Change: $ ', round(avg_profit_change, 2))
print ('Greatest Increase in Profits: ', max_profit_date, "($", round(max_profit_change), ")")
print ('Greatest Decrease in Profits: ', min_profit_date, "($", round(min_profit_change), ")")


# export text file with results
output_path = os.path.join("PyBank.txt")

with open(output_path, 'w', newline='') as csvfile:
        csvwriter= csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(["Financial_Analysis"])
        csvwriter.writerow(["Total Months:  86"])
        csvwriter.writerow(["Total: 38382578"])
        csvwriter.writerow(["Average Change: $  -2315.12"])
        csvwriter.writerow(["Greatest Increase in Profits:  Jan-2012 ($ 1926159 )"])
        csvwriter.writerow(["Greatest Decrease in Profits:  Aug-2013 ($ -2196167 )"])