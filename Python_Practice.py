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
        
        #Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)
    
print(candidate_options)