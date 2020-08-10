import os
import csv

#define variables
total_months = 0
net_revenue = 0
revenue_average = 0
revenue_change = 0
month_change = []
month = []
month_count = []

# Path to collect data from the Resources folder
bank_data = os.path.join('Resources', 'budget_data.csv')
# Define the function and have it accept the 'bank_data' as its sole parameter

def totals(bank_data):
    # assign your values to variables with descriptive names
    month = str(bank_data[0])
    revenue = int(bank_data[1])

# Read in the CSV file
with open(bank_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Don't read the header
    csvheader = next(csvreader)
    row = next (csvreader)
 
 # Set variables within rows
    total_months += 1
    net_revenue = int(row[1])
    previous_revenue = int(row[1])
    greatest_inc = int(row[1])
    greatest_inc_month = row[0]
    greatest_dec = int(row[1])
    greatest_dec_month = row[0]

# Start forloop
    for row in csvreader:
# Count number of months in file
        month.append(row[0])
        month_count = len(month)

    # Net profits/losses over entire time frame
        net_revenue += int(row[1])

    # Find the monthly change values
        revenue_change = int(row[1]) - previous_revenue
        month_change.append(revenue_change)

    # Average the changes of the profits/losses over the entire timeframe
        revenue_average = int(net_revenue) / int(month_count)

    # Find the greatest increase of profit
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            # List the date and amount for greatest increase of profit        
            greatest_inc_month = row[0]

    # Find the greatest decrease of profit
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            # List the date and amount for greatest decrease of profit
            greatest_dec_month = row[0]

    highest_rev = max(month_change)
    lowest_rev = min(month_change)

#print statements
print(f"Financial Analysis")
print(f"------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${net_revenue}")
print(f"Average Change: {revenue_average}")
print(f"Greatest Inc in Profits: {greatest_inc_month}, {highest_rev}")
print(f"Greatest Dec in Profits: {greatest_dec_month}, {lowest_rev}")

bank_data.close()