import os
import csv

#define variables to 0 or []


# Path to collect data from the Resources folder
bank_data = os.path.join('Resources', 'election_data.csv')

# Define the function and have it accept the 'election_data' as its sole parameter

def poll_results(election_data):
    # assign your values to variables with descriptive names
    voter_id = float(election_data[0])
    county = str(election_data[1])
    candidate = str(election_data[2])

# Read in the CSV file
with open(e;e_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Don't read the header
    csvheader = next(csvreader)
    row = next (csvreader)
 
 # Set variables within rows (+=, row[])


# Start forloop
    for row in csvreader:

    #total number of votes cast (count the Voter_IDs)

    #List of Candidates who received votes

    #Percentage of votes each candidate won

    #Winner

#print statements
print(f"Election Results")
print(f"------------------------")
print(f"Total Votes: {vote_count}")
print(f"Total: ${net_revenue}")
print(f"Average Change: {revenue_average}")
print(f"Greatest Inc in Profits: {greatest_inc_month}, {highest_rev}")
print(f"Greatest Dec in Profits: {greatest_dec_month}, {lowest_rev}")

  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```


#export txt file
