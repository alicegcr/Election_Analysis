# # The data we need to retrieve
# # 1. The total number of votes cast
# # 2. A complete list of candidates who received votes
# # 3. The percentage of votes each candidate won
# # 4. The total number of votes each candidate won 
# # 5. The winner of the election based on popular vote


# # Import the datetime class from the datetime module 
# import datetime
# from distutils import text_file
# # Use the now() attribute  on the datetime class to get the present time 
# now = datetime.datetime.now()
# # Print the present time 
# print("The time right now is", now)

# import csv
# dir (csv)

# import os
# os.listdir()

# # Assign a variable for the file to load and the path 
# file_to_load = '/Users/alicetamiazzo/Desktop/Election_Analysis/Resources/election_results.csv'

# # Open the election results and read the file 
# with open(file_to_load) as election_data:

#      # To do: perform analysis 
#      print(election_data)

# # Close the file
# election_data.close()

# # Create a filename variable to direct or indirect path where the file is to be located 
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() with 'w' mode we will write data to the file 
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file 
#     txt_file.write("Arapaho\nDenver\nJefferson")

# # Close the file 
# txt_file.close()

# Add our dependencies 
import csv
import os
# assign a variable to open the file 
file_to_load = '/Users/alicetamiazzo/Desktop/Election_Analysis/Resources/election_results.csv'
# Assign a variable to save the file path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initilize the total votes counter 
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each row in the CSV File
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Get the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list 
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's vote count 
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's count 
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:    
    #Print the final vote count to the terminal 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)
    #Determine the percentage of votes for each candidate by looping through he counts:
    # 1. iterate through the candidate list:
    for candidate_name in candidate_votes:
        #2. Retrieve vote count and percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results =(
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


        # Print each candidate's voter count and percentage to the terminal 
        print(candidate_results)
        # Save the candidate's results to the text file 
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate 
        # 1.Determine if the votes is greater than the winning count 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set the winning count = vote and winning percentage = 
            # vote percentage 
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name 
            winning_candidate = candidate_name
    # Print the winning candidate's results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)

      
            






 

   







