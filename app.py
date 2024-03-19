# Read the number of blank, null, and valid votes
num_blank_votes = int(input("Enter the number of blank votes: "))
num_null_votes = int(input("Enter the number of null votes: "))
num_valid_votes = int(input("Enter the number of valid votes: "))

# Calculate the total number of votes
total_votes = num_blank_votes + num_null_votes + num_valid_votes

# Calculate the percentage of each type of vote
percent_blank_votes = (num_blank_votes / total_votes) * 100
percent_null_votes = (num_null_votes / total_votes) * 100
percent_valid_votes = (num_valid_votes / total_votes) * 100

# Write the percentage of each type of vote
print("Percentage of blank votes: {:.2f}%".format(percent_blank_votes))
print("Percentage of null votes: {:.2f}%".format(percent_null_votes))
print("Percentage of valid votes: {:.2f}%".format(percent_valid_votes))