# Example outcome 
 # Financial Analysis
 # ----------------------------
 # Total Months: 86
 # Total: $38382578
 # Average  Change: $-2315.12
 # Greatest Increase in Profits: Feb-2012 ($1926159)
 # Greatest Decrease in Profits: Sep-2013 ($-2196167)


# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period


import os
import csv

with open("budget_data.csv") as file:
    read_file=csv.reader(file)
    csvreader=list(read_file)
    csvreader_header=csvreader[0]
    #select second row and everything after using :
    csvreader=csvreader[1:]

total=0 

for row in csvreader:
    row_count = len(csvreader)-1

    total += int(row[1])

    # nest an if statement to compare each row to print the greatest increase
    inc= max(str(row[1]))
    
    # nest an if statement to compare each row to print the greatest decrease
    dec= min(str(row[1]))

    # mean of the change from month to month
    # create list for average change and append. 
    # first row is not a change so "pop" the first row 
    Avg = int(total/row_count)
    

print(f'Total Months: {row_count+1}')
print (f'Total: {total}')
print (f'Average: {Avg}')
print (f'Greatest Increase in Profits: ({inc})')
print (f'Greatest Decrease in Profits: ({dec})')


# export text file with results