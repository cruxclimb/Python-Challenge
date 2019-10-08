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

# Path to collect data from the homework folder
pyBank_csv =  os.path.join('budget_data.csv')


# Define the function and have it accept the 'bank_data' as its sole parameter


# Print the analysis
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {#insert months here}')
    print(f'Total: {#insert total here}')
    print(f'Average: {#insert average change here}')
    print(f'Greatest Increase in Profits: {#insert month-year amount in () here}')
    print(f'Greatest Decrease in Profits: {#insert month-year amount in () here}')

# Export a .txt file with the results

# Read in the CSV file
with open(pyBank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader: