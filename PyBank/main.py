import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join('Resources', 'budget_data.csv')

# Define the function and have it accept the 'daterow' as its sole parameter
def profit_loss(row):
    # For readability, it can help to assign your values to variables with descriptive names
    date = str(row[0])
    transactions = long(row[1])

# Read in the CSV file
with open(budget_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
