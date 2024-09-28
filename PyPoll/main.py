# Import necessary modules
from csv import reader, DictReader, writer, DictWriter
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# initialize 3 lists: votes, candidates & final_list
#votes list will contain all the ballot IDs; candidates list will contain the candidate names (multiple occurences)
#final_list is a list containg dictionary with details on every candidate
votes = []
candidates = []
final_list = []

#open dataset file to read
with open(file_to_load) as file1:
    csv_reader = reader(file1)
    next(csv_reader)

    for row in csv_reader:
        votes.append(row[0])
        candidates.append(row[2])
    
    total_votes= len(votes)
    candidate_list = list(set(candidates))
    
    #creating a list of dict with all details on every candidate
    for item in candidate_list:
        final_list.append({"name" : item, "vote_count": candidates.count(item), "vote_percent": round((candidates.count(item)/len(candidates))*100 , 3)})
    # isolating vote percent info from final_list and calculating the max value
    max_percent = max([item['vote_percent'] for item in final_list ])
    
    # find the candidate with maximum vote percent/count    
    for item in final_list:
        if item["vote_percent"] == max_percent:
            item["winner"] = True
        else:
            item["winner"] = False
            
    # print results to terminal
    print("Election Results\n")
    print("---------------\n")
    print(f"Total Votes: {total_votes}\n")
    print("----------------\n")
    for item in final_list:
        print(f"{item['name']}: {item['vote_percent']}% ({item['vote_count']})\n")
    print("-----------------\n")
    for item in final_list:
        if item["winner"] == True:
            print(f"Winner: {item['name']}\n")
    print("------------------")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-----------------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-----------------------------------\n")
    for item in final_list:
        txt_file.write(f"{item['name']}: {item['vote_percent']}% ({item['vote_count']})\n")
    txt_file.write("-----------------------------------\n")
    for item in final_list:
        if item["winner"] == True:
            txt_file.write(f"Winner: {item['name']}\n")
    txt_file.write("-----------------------------------")

            



    
    
    
 