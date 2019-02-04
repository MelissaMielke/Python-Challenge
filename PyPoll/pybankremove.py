### PyBank
##Requirement: Analyze company finance via csv file = 'budget_data.csv'
    ##File has 2 columns: 'Date' (Mon-YY) and 'Profit/Losses' (integer)
    ##File has 87 rows; first row is column headers (skip in counts)

# Import Modules: 'pathlib' to access / 'csv' to read file
from pathlib import Path
import csv

# Set path for 'budget_data' CSV file *assume in CWD*
inpath = ('budget_data.csv')

#Open csv file in 'read mode' at defined path variable
with open(inpath, newline='') as csvfile:

    #Read csv file; delimiter 'comma'
    readcsv = csv.reader(csvfile, delimiter=',')
    #Skip row one as 'header'
    next(readcsv, None)

    #Create empty lists for column data: date, profit/loss (prls)
    ls_date = []
    ls_prls = []

    #Create and initialize total variables
    tot_date = 0
    tot_prls = 0

    #Loop thru remaining rows in csv file
    for row in readcsv:

        #Calculate totals for each column
        tot_date += 1
        tot_prls += int(row[1])

        #Append row values to lists
        ls_date.append(row[0])
        ls_prls.append(int(row[1]))

    #Create empty list for diff in profit from month/month
    ls_diff = []

    for i in range(1,len(ls_prls)): 

        #Append difference in profit value to list
        ls_diff.append(int(ls_prls[i]) - int(ls_prls[i-1]))

    #Calculate average profit change
    ave_diff = round(sum(ls_diff)/len(ls_diff), 2)

    #Determine greatest profit increase/decrease
    max_diff = max(ls_diff)
    min_diff = min(ls_diff)

    #Determine indexes of max/min averages
    max_id = ls_diff.index(max_diff)
    min_id = ls_diff.index(min_diff)

    #Determine date of max/min averages
    max_date = ls_date[max_id + 1]
    min_date = ls_date[min_id + 1]

    #Print output to command line
    print('Period Financial Analysis:')
    print('--------------------------------------------------')
    print(f'Total Month Count: {tot_date}')
    print(f'Total Profit Amount: ${tot_prls}')
    print(f'Average Profit Change: ${ave_diff}')
    print(f'Greatest Profit Increase: {max_date} (${max_diff})')
    print(f'Greatest Profit Decrease: {min_date} (${min_diff})')

# Set path for 'budget_data' CSV file *assume in CWD*
outpath = ('pybank_out.txt')

#Open csv file in 'write mode' to copy results to file
with open(outpath, 'w') as new:
    new.write('Period Financial Analysis:\n')
    new.write('--------------------------------------------------\n')
    new.write(f'Total Month Count: {tot_date}\n')
    new.write(f'Total Profit Amount: ${tot_prls}\n')
    new.write(f'Average Profit Change: ${ave_diff}\n')
    new.write(f'Greatest Profit Increase: {max_date} (${max_diff})\n')
    new.write(f'Greatest Profit Decrease: {min_date} (${min_diff})\n')
    new.close()
