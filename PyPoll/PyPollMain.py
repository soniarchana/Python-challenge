import os
import csv

# Define Poll Dictionary with three keys 
myPollDict = {"Candidates": [], 
"Total_Votes": [], 
"Percent": [] 
}

# Define the lists
MyCandidates = []
Vote_Cnt = []
Vote_Per = []
# Initializing Variables
Tot_Votes = 0
i = 0

# Setting file path
csvpath = "/Users/archana/Documents/PREWORK_AS/Module-3/Resources/election_data.csv"
csvwpath = "/Users/archana/Desktop/Python-challenge/PyPoll/PyPollout.csv"


print("Election Results")
print("--------------------------------------")

# Open file to read and analyze 
with open(csvpath, newline="") as csvfile:
	csvreader =  csv.reader(csvfile, delimiter=",")
	
	# Skipping the header row
	next(csvreader, None)
    
    # Opening output file for writing output
	with open(csvwpath, "w", newline="") as csvwfile:
		csvwriter = csv.writer(csvwfile, delimiter=",")
		# Writing header row to output file	
		csvwriter.writerow(['Election Results', '', ''])
		csvwriter.writerow(['--------------------------------------', '', ''])


		# Compute Total Votes and print
		Tot_Votes = sum(1 for row in csvfile)
		print("Total Votes: " + str(Tot_Votes) if Tot_Votes else 'No rows - The file is empty')
		print("--------------------------------------")

		# Writing output to output file
		csvwriter.writerow(['Total Votes: ', str(Tot_Votes) if Tot_Votes else 'No rows - The file is empty', ''])
		csvwriter.writerow(['--------------------------------------','', ''])

		# Go to beginning of file 
		csvfile.seek(0)

		# Skipping the header row
		next(csvreader, None)

		# Compute the unique Candidates and store in Candidates list and initialize the Vote_Cnt and Vote_Per list with 0
		for row in csvreader:
			if row[2] not in MyCandidates:
				MyCandidates.append(row[2])
				Vote_Cnt.append(0)
				Vote_Per.append(0.0)

		# Go to beginning of file 
		csvfile.seek(0)

		# Loop to calulate the Total votes and Percent for each candidates and store in respective list
		for cnt_vts_row in csvreader:
			for i in range(0, len(MyCandidates)):
				if cnt_vts_row[2] == MyCandidates[i]:
					Vote_Cnt[i] += 1
					Vote_Per[i] = float((100/Tot_Votes)*Vote_Cnt[i])

		# Find the Winner Percent
		WinnerPer= max(Vote_Per)
		#print("{0:.2f}".format(WinnerPer))

		# Store lists in Dictionary
		myPollDict["Candidates"]= MyCandidates
		myPollDict["Total_Votes"]=Vote_Cnt
		myPollDict["Percent"]=Vote_Per

		p=0.0
		# Print the Candidates with Percent and Total Votes
		for k in range(0, len(MyCandidates)):
			p="{0:.2f}".format(Vote_Per[k])
			print(MyCandidates[k], " :", p, " (", Vote_Cnt[k], ")")
			csvwriter.writerow([MyCandidates[k]+ " : ", p, " ("+ str(Vote_Cnt[k])+")"])

		print("--------------------------------------")
		csvwriter.writerow(['--------------------------------------','', ''])
		# Find the winner Candidate and print
		for w in range(0, len(Vote_Per)):
			if Vote_Per[w] == WinnerPer:
				print("Winner :" + str(MyCandidates[w]))
				csvwriter.writerow(['Winner :', str(MyCandidates[w])])
		print("--------------------------------------")
		csvwriter.writerow(['--------------------------------------','', ''])
