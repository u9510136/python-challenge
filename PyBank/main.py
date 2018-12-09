import os
import csv

month_count = 0
total_sum = 0
inc_max_month = ""
dec_min_month = ""
inc_max = 0
dec_min = 0 

# Read Data from .csv file
bank_csv = os.path.join("budget_data.csv")

with open(bank_csv, "r", encoding = "UTF-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:

        month_count += 1
        total_sum += int(row[1]) # Count for set of data

        if int(row[1]) > inc_max:
            
            inc_max = int(row[1])
            inc_max_month = row[0] # find the greatest increase 

        elif int(row[1]) < dec_min:

            dec_min = int(row[1])
            dec_min_month = row[0] # find the greatest decrease

#print out the result    
print("Financial Analysis")
print("---------------------------------")
print("Total months: " + str(month_count))
print("Total: $" + str(total_sum))
print("Average Change: $" + str(round(total_sum/month_count, 2)))
print("Greatest Increase in Profits: " + inc_max_month + " ($" + str(inc_max) + ")")
print("Greatest Decrease in Profits: " + dec_min_month + " ($" + str(dec_min) + ")")

#export the result into a new csv file
op_path = os.path.join("finacial_analysis.csv")

with open(op_path, "w", newline = "", encoding = "UTF-8") as datafile:

    writer = csv.writer(datafile, delimiter=',')

    writer.writerow(["Financial Analysis"])
    writer.writerow(["Totla months", month_count])
    writer.writerow(["Total", total_sum])
    writer.writerow(["Average Change",round(total_sum/month_count, 2)])
    writer.writerow(["Greatest Increase in Profits",inc_max_month,inc_max])
    writer.writerow(["Greatest Decrease in Profits",dec_min_month,dec_min])