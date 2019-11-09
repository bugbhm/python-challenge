# imports
import os
import csv

# read csv
csv_file = os.path.join('election_data.csv')

# list to store data
percent_votes = 0
total_votes = 0
correy_votes = 0
khan_votes = 0
li_votes = 0
otooley_votes = 0

winner = []

# read data in file
with open(csv_file,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_votes = total_votes + 1

    # start loop to count candidate votes
    for row in csvreader:
        total_votes = total_votes + 1
        
        #total votes per candidate
        if row[2] == 'Correy':
            correy_votes = correy_votes + 1
        elif row[2] == 'Khan':
            khan_votes = khan_votes +1
        elif row[2] == 'Li':
            li_votes = li_votes +1
        else: otooley_votes = otooley_votes + 1

#calculate percents
correy_percent = correy_votes / total_votes
khan_percent = khan_votes / total_votes
li_percent = li_votes / total_votes
otooley_percent = otooley_votes / total_votes

#find winner
winner = max(correy_votes, khan_votes, li_votes, otooley_votes)

if winner == correy_votes:
    winner_name = "Correy"
elif winner == khan_votes:
    winner_name = "Khan"
elif winner == li_votes:
    winner_name = "Li"
else: winner_name = "O'Tooley"

# print
print(f'Election Results')
print('------------------------------')
print(f'Total Votes: {total_votes}')
print('------------------------------')
print(f"Kahn: {khan_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

#output
pypoll_file = os.path.join('PyPoll_results.txt')

#Specify the file to write to
with open(pypoll_file, 'w') as results_csv:
    results_csv.write(f"Election Results\n")
    results_csv.write(f"---------------------------\n")
    results_csv.write(f"Total Votes: {total_votes}\n")
    results_csv.write(f"---------------------------\n")
    results_csv.write(f"Kahn: {khan_percent:.3%}({khan_votes})\n")
    results_csv.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    results_csv.write(f"Li: {li_percent:.3%}({li_votes})\n")
    results_csv.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    results_csv.write(f"---------------------------\n")
    results_csv.write(f"Winner: {winner_name}\n")
    results_csv.write(f"---------------------------\n")