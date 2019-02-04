### PyPoll
##Requirement: Modernize rural voting by analyzing 'election_data.csv'
##File Columns= 3: 'Voter ID', 'County', 'Candidate'
##File Rows= 3 million+: too large for Excel, could only view sample

# Import Modules: 'pathlib' access / 'csv' read file
from pathlib import Path
import csv

# Set path for 'election_data' CSV file *assume in CWD*
inpath = ('election_data.csv')

#Open csv file in 'read mode' at defined path variable
with open(inpath, newline='') as csvfile:

    #Read csv file; delimiter 'comma'
    readcsv = csv.reader(csvfile, delimiter=',')

    #Initialize variables, lists, dictionaries to hold csv data 
    tot_vote = 0
    win_vote = 0
    all_vote = []
    all_cand = []
    dct_cand = {}

    #Skip row one as 'header'
    next(readcsv, None)

    #Loop thru rows in csv file (start row 2)
    for row in readcsv:
        
        #Calculate total vote count
        tot_vote += 1

        #Compile list of unique candidate names
        if row[2] not in all_cand:
            all_cand.append(row[2])
           
            #Define candidate name as key
            dct_cand[row[2]] = 0
            dct_cand[row[2]] = dct_cand[row[2]] + 1
        
        else:
            dct_cand[row[2]] += 1

    #Begin print results to command line
    print('Election Poll Results:')
    print('---------------------------------------')
    print(f'Total Votes Counted: {str(tot_vote)}')
    print('---------------------------------------')

    #Loop thru candidate dictionary, get vote count/percent
    for all_cand in dct_cand:
        all_vote = dct_cand.get(all_cand)
        perc_vote = round((all_vote / tot_vote), 3)*100
        
        #Print candidate dictionary results to command line 
        print(f'{all_cand}:  {perc_vote}%  ({all_vote})')
        if all_vote > win_vote:
            win_vote = all_vote
            win_cand = all_cand

print('----------------------------------------') 
print(f'Election Winner:  {win_cand}')

# Set path for 'budget_data' CSV file *assume in CWD*
outpath = ('pypoll_out.txt')

#Open csv file in 'write mode' to copy results to file
with open(outpath, 'w') as new:
    new.write('Election Poll Results:\n')
    new.write('----------------------------------\n')
    new.write(f'Total Votes Counted: {str(tot_vote)}\n')
    new.write('----------------------------------\n')
    
    for all_cand in dct_cand:
        all_vote = dct_cand.get(all_cand)
        perc_vote = round((all_vote / tot_vote), 2)*100
        new.write(f'{all_cand}:  {perc_vote}%  ({all_vote})')

    new.write('----------------------------------------\n')
    new.write(f'Election Winner:  {win_cand}\n')
    new.close()
