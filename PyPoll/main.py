import os
import csv


with open("election_data.csv") as file:
    read_file=csv.reader(file)
    
    next(read_file)
    candidate = []


    next(read_file)
    for row in read_file:
        # candidate = line[-1]
        # votes[candidate] += 1

        candidate.append(row[0])
        total_votes= len(candidate)
        

print("Election Results")
print("------------------------------------------")
print(f'Total Votes: {total_votes}')
print("------------------------------------------")
print(f'Khan: % ( )')
print(f'Correy: % ( )')
print(f'Li: % ( )')
print(f'OTooley: % ( )')
print("------------------------------------------")
print (f'Winner: % ( )')
print("------------------------------------------")

