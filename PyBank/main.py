# imports
import os
import csv

# read csv
csv_file = os.path.join('budget_data.csv')

# list to store data
total_change = []
greatest_increase = []
greatest_decrease = []

total_months = 0
total_ProfitLoss = 0

greatest_increase = 0
greatest_decrease = 999999999

monthly_increase = []
monthly_decrease = []
previous_net = 0

# print header
print(f'Financial Analysis')
print('------------------------------')

# data in the file
with open(csv_file,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Header row
    csv_header = next(csvreader)

    # read data
    first_row = next(csvreader)
    total_months = total_months + 1
    total_ProfitLoss = total_ProfitLoss + int(first_row[1])
    previous_net = previous_net + int(first_row[1])

    # loop through csv
    for row in csvreader:

        total_months = total_months + 1
        total_ProfitLoss = total_ProfitLoss + int(row[1])        
        net_change = int(row[1]) - int(previous_net)
        previous_net = int(row[1])

        total_change = total_change + [net_change]
        average_net_change = round(sum(total_change) / len(total_change))

        # greatest profit
        if net_change > greatest_increase:
            monthly_increase = row[0]
            greatest_increase = net_change

        # greatest loss
        if net_change < greatest_decrease:
            monthly_decrease = row[0]
            greatest_decrease = net_change
        
        
# Print results
print(f'Total Months: {total_months}')
print(f'Total: ${total_ProfitLoss}')
print(f'Average Change: ${average_net_change}')
print(f'Greatest Profit: {monthly_increase}, ${greatest_increase}')
print(f'Greatest Loss: {monthly_decrease}, ${greatest_decrease}')

# output
pybank_output = os.path.join('PyBank_results.txt')

# Write to text file
with open(pybank_output, 'w') as results_csv:
    results_csv.write(f'Financial Analysis\n')
    results_csv.write('------------------------------\n')
    results_csv.write(f'Total Months: {total_months}\n')
    results_csv.write(f'Total: ${total_ProfitLoss}\n')
    results_csv.write(f'Average Change: ${average_net_change}\n')
    results_csv.write(f'Greatest Profit: (${greatest_increase}\n)')
    results_csv.write(f'Greatest Loss: (${greatest_decrease}\n)')
