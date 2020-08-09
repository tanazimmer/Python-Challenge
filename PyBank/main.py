import os
import csv

# Path to collect data from the Resources folder
bank_data = os.path.join('Resources', 'budget_data.csv')

# Define the function and have it accept the 'bank_data' as its sole parameter
def totals(bank_data):
    # For readability, it can help to assign your values to variables with descriptive names
    month = str(bank_data[0])
    revnue = int(bank_data[1])


# Read in the CSV file
with open(bank_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    month = []
    revenue = []
    revenue_diff = []


# Count number of months in file
    for row in csvreader:
        month.append(row[0])
    print(len(month))

# Net profits/losses over entire timeframe
    for row in csvreader:
        revenue.append(row[1])

# Average the changes of the profits/losses over the entire timeframe

# Find the greatest increase of profit

# List the date and amount for greatest increase of profit

# Find the greatest decrease of profit

# List the date and amount for greatest decrease of profit





    # Loop through the data

