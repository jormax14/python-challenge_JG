import os
import csv

#define csv path
election_path = os.path.join("..", "..", "..", "RICEHOU201811DATA2", "class-tth", "03-Python", "homework", "Instructions", "PyPoll", "Resources", "election_data.csv")

#read in the csv file
with open(election_path, "r",newline="") as election_csv:

    election_reader = csv.reader(election_csv, delimiter=",")
    election_header = next(election_reader)
    
#set inital variables and blank lists
    voter_count = 0
    candidate_data = []
    candidates = {}
    candidates_percentage = {}
    combined_data = {}

#loop for total voter count and populate candidate_data list
    for row in election_reader:
        voter_count +=1
        candidate_data.append(row[2])

#loop through candidate_data list to count occurence of key to populate candidates dictionary
    for x in candidate_data:
        if x in candidates:
            candidates[x] = candidates.get(x) + 1
        else:
            candidates[x] = 1

#define/populate candidates_percentage dictionary by looping through candidates dictionary and turning voter count into %
    candidates_percentage = {k: round(v / voter_count * 100, 3) for k, v in candidates.items()}

#combine candidates and candidates_percentage dictionary into one dictionary
    for key in (candidates.keys() | candidates_percentage.keys()):
        if key in candidates: combined_data.setdefault(key, []).append(candidates[key])
        if key in candidates_percentage: combined_data.setdefault(key, []).append(candidates_percentage[key])

#define winner from key in candidates based on max value            
    winner = max(candidates, key=candidates.get)
    
#print results
print(f"Election Results")
print(f"-"*25)
print(f"Total Votes: {voter_count}")
print(f"-"*25)

for k, (v, z) in combined_data.items():
    print(f"{k}: {z}00% ({v})")
    
print(f"-"*25)
print(f"Winner: {winner}")
print(f"-"*25)

with open("main_output_JG.txt","w") as txtfile:
    print(f"Election Results", file=txtfile)
    print(f"-"*25, file=txtfile)
    print(f"Total Votes: {voter_count}", file=txtfile)
    print(f"-"*25, file=txtfile)

    for k, (v, z) in combined_data.items():
    print(f"{k}: {z}00% ({v})", file=txtfile)
    
    print(f"-"*25, file=txtfile)
    print(f"Winner: {winner}", file=txtfile)
    print(f"-"*25, file=txtfile)