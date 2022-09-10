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
from email import header
import os

# assign a variable to open the file 
file_to_load = '/Users/alicetamiazzo/Desktop/Election_Analysis/Resources/election_results.csv'
# Assign a variable to save the file path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyse the data here 
    # Read the file object with the reader function 
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)
    print(header)


    # # Print each row to csv file 
    # for row in file_reader:
    #     print(row)

   







