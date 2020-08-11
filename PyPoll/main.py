import os
import csv

#define variables to 0 or []
vote_count = []
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
voter_id = []
winner = []
candidate = []
winning_candidate = []

# Path to collect data from the Resources folder
election_data = os.path.join('Resources', 'election_data.csv')

# Define the function and have it accept the 'election_data' as its sole parameter

def poll_results(election_data):
    # assign your values to variables with descriptive names
    voter_id = float(election_data[0])
    county = str(election_data[1])
    candidate = str(election_data[2])

# Read in the CSV file
with open(election_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Don't read the header
    csvheader = next(csvreader)
    row = next (csvreader)
 
 # Set variables within rows (+=, row[])

# Start forloop
    for row in csvreader:

    #total number of votes cast (count the Voter_IDs)
        voter_id.append(row[0])
        vote_count = len(voter_id)

    #List of Candidates who received votes?????

    #Percentage of votes each candidate won

        if (row[2]== "Khan"):
            khan_votes += 1
        elif (row[2]== "Correy"):
            correy_votes += 1
        elif (row[2]== "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

    khan_percent = khan_votes / vote_count
    correy_percent = correy_votes / vote_count
    li_percent = li_votes / vote_count
    otooley_percent = otooley_votes / vote_count

    #Winner
    winner = max(khan_percent, correy_percent, li_percent, otooley_percent)

    if winner== khan_percent:
        winning_candidate = "Khan"
    elif winner== correy_percent:
        winning_candidate = "Correy"
    elif winner== li_percent:
        winning_candidate = "Li"
    else:
        winning_candidate = "O'Tooley"

#print statements
print(f"Election Results")
print(f"------------------------")
print(f"Total Votes: {vote_count}")
print(f"Khan: {khan_percent: .3%} ({khan_votes})")
print(f"Correy: {correy_percent: .3%} ({correy_votes})")
print(f"Li: {li_percent: .3%} ({li_votes})")
print(f"O'Tooley: {otooley_percent: .3%} ({otooley_votes})")
print(f"------------------------")
print(f"Winner: {winning_candidate}")


#export txt file
election_analysis = os.path.join('Analysis', 'election_analysis.txt')
with open(election_analysis, 'w',) as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Total Votes: {vote_count}\n")
    txtfile.write(f"Khan: {khan_percent: .3%} ({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent: .3%} ({correy_votes})\n")
    txtfile.write(f"Li: {li_percent: .3%} ({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent: .3%} ({otooley_votes})\n")
    txtfile.write(f"------------------------\n")
    txtfile.write(f"Winner: {winning_candidate}\n")