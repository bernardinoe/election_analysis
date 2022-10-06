# The data we need to retreive
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes.

#Direct Path
#import csv

#file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file
#with open(file_to_load) as election_data:

     # To do: perform analysis.
#     print(election_data)

# Indirect Path
#import os
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
#     print(election_data)


#Create a file
# Create a filename variable to a direct or indirect path to the file.
##file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
##open(file_to_save, "w")


#Write on file
#Shorter Code
# Create a filename variable to a direct or indirect path to the file.
##file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
##with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
     # Write three counties to the file.
##    txt_file.write("Counties in the Election\n") 
##    txt_file.write("------------------------\n")
##    txt_file.write("Arapahoe\nDenver\nJefferson")


##3.4.4
    # Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
        file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
        ##for row in file_reader:
        ##    print(row[0])
    # Print the header row.
        headers = next(file_reader)
        print(headers)        
