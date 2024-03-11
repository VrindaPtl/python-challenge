# Dependencies
import csv

# Files to load and Output
file_to_load = "/Users/vrindapatel/Desktop/Homework/W3 Python challenge/python-challenge/PyPoll/Resources/election_data.csv"
file_to_output = "/Users/vrindapatel/Desktop/Homework/W3 Python challenge/python-challenge/PyPoll/Analysis/PyPoll_Analysis.txt"


# Total Vote Counter
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

# Open the CSV file
with open(file_to_load) as election_data:
    csv_reader = csv.DictReader(election_data)

    # Iterate through each row in the CSV
    for row in csv_reader:
        
        # Calculate the total number of votes
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row["Candidate"]

        # 3. If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # 4. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

        #print the result and export to text file
        with open(file_to_output, "w") as txt_file:

            # Print the final vote count (to terminal)
            election_results = (
                f"\n\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"-------------------------\n")
            print(election_results)
            txt_file.write(election_results)

            # Determine the percentage of votes for each candidate by looping through the counts
            
            for candidate in candidate_votes:   

                # Retrieve vote count of a candidate and percentage
                votes = candidate_votes.get(candidate)
                vote_percentage = float(votes) / float(total_votes) * 100

                # Determine winning vote count and candidate
                if (votes > winning_count):
                    winning_count = votes
                    winning_candidate = candidate

                # Print out each candidate's vote count, and percentage of votes
                voter_output = (f"{candidate}: {vote_percentage:.3f}% ({votes:,})\n")
                print(voter_output)

                # save voter count to text file
                txt_file.write(voter_output)

            # Print the winning candidate (to terminal)
            winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"-------------------------\n")
            print(winning_candidate_summary)

            # save the analysis to text file
            txt_file.write(winning_candidate_summary)