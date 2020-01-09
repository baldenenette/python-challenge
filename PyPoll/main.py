import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
pathout = os.path.join("Resources", "Election Analysis")

candidate_votes = 0
candidate_results = {}
vote_percentage = 0
total_votes = 0
winner = ""
candidate_list=[]
candidat_value = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    next(csvreader)

    #looping

    for row in csvreader:

        total_votes += 1
        candidate = row[2]

        if candidate  not in candidate_list:
            candidate_list.append(candidate)
            candidate_results[candidate] = 1
        else:
            candidate_results[candidate] +=  1
    print("Election Results")
    print("-------------------------")
    print(total_votes)
    print("-------------------------")
    
    for candidate in candidate_list:
        print((candidate) + " (" + str(candidate_results[candidate]) + ") "+ str((candidate_results[candidate]/total_votes)*100) + "%")
        candidat_value.append(candidate_results[candidate])
    print("-------------------------")
    winner = max(candidat_value)
    for candidate in candidate_list:
        if winner == candidate_results[candidate]:
            print("The winner is: " + candidate)
    print("-------------------------")
    #print(winner)       
    #print(candidate_list)
   # print("got it")
   