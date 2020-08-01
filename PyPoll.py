# The data we need to retrieve.
#1. The total number of votes
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote


#Add our dependencies.
import csv
import os

#Assign a variable to load a file from a path.
polling_data = os.path.join("election_results.csv")
#Assign a variable to save the file to a path.
saved_polling_data = os.path.join("analysis","election_analysis.txt")

#Initialize the total vote counter.

total_votes = 0

#Declare new list for candidate options
candidate_options = []

#Declare a voting dictionary.
candidate_votes = {}

winning_candidate = ""

winning_count = 0

winning_percentage = 0 

#Open the election results and read the file
with open(polling_data) as election_data:

    file_reader = csv.reader(election_data)
    
    #Read the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        
        #Print the candidate name from each row.
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] += 1
    
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes)*100
        
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        if (votes > winning_count) and (vote_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count:{winning_count:,}\n"
        f"Winning Percentage:{winning_percentage:.1f}%\n"
        f"-------------------------------\n")

    
    print(winning_candidate_summary)