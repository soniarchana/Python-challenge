def ave1 (no): 
	dil = []
	a=1
	for i in no:
		dil.append(int(no[a]) - int(i))
		a=a+1
		if (a == len(no)):
			break
	return dil


import os
import csv

# Setting file path
csvpath = "/Users/archana/Documents/PREWORK_AS/Module-3/Resources/budget_data.csv"
csvwpath = "/Users/archana/Desktop/Python-challenge/PyBank/PyBankout.csv"

# Initializing Variables
Avg_ChangeCol = []
MonYr_Col = []
Avg_Change = []
Tot_Months = 0
Tot_Net_Amt= 0
Gr_Inc = 0
Gr_Dec = 0

# Open file to read and analyze 
with open(csvpath, newline="") as csvfile:
	csvreader =  csv.reader(csvfile, delimiter=",")
	
	# Skipping the header row
	next(csvreader, None)

	#tot_months = sum(1 for row in csvfile)
	#print("The total number of months included in the dataset :" + str(Tot_Months) if Tot_Months else 'No rows - The file is empty')

	# Opening output file for writing output
	with open(csvwpath, "w", newline="") as csvwfile:
		csvwriter = csv.writer(csvwfile, delimiter=",")
		# Writing header row to output file	
		#csvwriter.writerow (['Summary Details', 'Summary Value'])
		csvwriter.writerow(['Financial Analysis', ''])
		csvwriter.writerow(['----------------------------------------------------', ''])


		# Loop to traverse through file
		for row in csvreader:
			Tot_Months = Tot_Months + 1
			Tot_Net_Amt = Tot_Net_Amt + int(row[1])
			Avg_ChangeCol.append( int(row[1]) )
			MonYr_Col.append( (row[0]) )
		
		print("  ")	
		print("Financial Analysis")
		print("---------------------------------------------------")
		print("Total Months: " + str(Tot_Months) if Tot_Months else 'No rows - The file is empty')
		print("Total: $" + str(Tot_Net_Amt))
		#print(Avg_ChangeCol) 

		Avg_Change= ave1(Avg_ChangeCol) 
		#print(Avg_Change)
		#print(MonYr_Col)

		if (int(len(Avg_Change)) != 0):
			print("Average Change: $", "{0:.2f}".format(sum(Avg_Change)/len(Avg_Change)))

			# Writing output Summary with Details to output file
			csvwriter.writerow(['Total Months:', str(Tot_Months) if Tot_Months else 'No rows - The file is empty'])
			csvwriter.writerow(['Total: $', str(Tot_Net_Amt)])
			csvwriter.writerow(['Average Change: $', "{0:.2f}".format(sum(Avg_Change)/len(Avg_Change))])

			Gr_Inc=max(Avg_Change)
			Gr_Dec=min(Avg_Change)

			itr=1
			for k in Avg_Change:
				if (k == int(Gr_Inc)):
					print("Greatest Increase in Profits: ", MonYr_Col[itr], "($",Gr_Inc,")")	
					csvwriter.writerow(['Greatest Increase in Profits:', str(MonYr_Col[itr])+" ($"+str(Gr_Inc)+")"])
				if (k == int(Gr_Dec)):
					print("Greatest Decrease in Profits: ", MonYr_Col[itr], "($",Gr_Dec,")")
					csvwriter.writerow(['Greatest Decrease in Profits:', str(MonYr_Col[itr])+" ($"+str(Gr_Dec)+")"])
					break
				else:
					itr=itr+1	
			print("---------------------------------------------------")
			csvwriter.writerow(['----------------------------------------------------',''])
