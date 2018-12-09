import os
import csv

total_vote = 0
can_name = ["Khan","Correy","Li","O'Tooley"]
can_vote = [0,0,0,0]
can_percent = [0,0,0,0]

# Read data from csv file
vote_csv = os.path.join("election_data.csv")

with open(vote_csv, "r", encoding = "UTF-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:

      # count every candidate's total vote 
      total_vote += 1
      if row[2] == can_name[0]:
        can_vote[0] += 1
      elif row[2] == can_name[1]:
        can_vote[1] += 1
      elif row[2] == can_name[2]:
        can_vote[2] += 1
      else:
        can_vote[3] += 1

# find the winner
if max(can_vote) == can_vote[0]:
    winner = can_name[0]
elif max(can_vote) == can_vote[1]:
    winner = can_name[1]
elif max(can_vote) == can_vote[2]:
    winner = can_name[2]
else:
    winner = can_name[3]

# print the result
print("Election Results")
print("--------------------------")
print("Total Votes: " + str(total_vote))
print("--------------------------")
for i in range(4):
    can_percent[i] = round(can_vote[i] * 100 / total_vote, 3)
    print(can_name[i] + ": " + str(can_percent[i]) + "% (" + str(can_vote[i]) + ")")
print("--------------------------")
print("Winner: " + winner)
print("--------------------------")

# zip dataset together
result = zip(can_name, can_percent, can_vote)

# export the result into a new csv file
wrpath = os.path.join(".","election.csv")

with open(wrpath, 'w', newline = '', encoding = "UTF-8") as datafile:

    writer = csv.writer(datafile, delimiter=',')

    writer.writerow(["Total Votes", total_vote, ""])
    writer.writerows(result)
    writer.writerow(["Winner", winner, ""])