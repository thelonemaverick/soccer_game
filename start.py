from operator import itemgetter
import csv
import os
import sys

###########################################
# Import getter to sort lists later  // import CSV to import data
##########################################

# We will divide the kids into 2 lists, rookie and veteran
# Later we will sort each list by height
# later when wee make teams they should be more fairly balanced with simlar skill lelvel and sizes
rookieslist = []
# rookie list (kids who have never played)

veteranslist = []
# experienced kids list


# open each CSV file with each line st a list.

with open('soccer_players.csv', newline='') as players:
        teamplayers = csv.reader(players, delimiter=',', quotechar='|')
# as we loop through each player - we assign each kid a list based on whether they have played or not.
        for player in teamplayers:
            if player[2] == "YES":
                veteranslist.append(player)
            elif player[2] == "NO":
                rookieslist.append(player)

# Extra credit - Sort each level of kid by height so they will be even experience-wise and height-wise
vetlist = sorted(veteranslist, key=itemgetter(1), reverse=True)
rooklist = sorted(rookieslist, key=itemgetter(1), reverse=True)

# Join both lists together for a final sort to 3 teams.
rank_sort = vetlist + rooklist
#  Use slices to pull every thirds kid in a staggered way.  3 slices, one for each team.
dragons = rank_sort[0::3]
sharks = rank_sort[1::3]
raptors = rank_sort[2::3]
###########################################
# Letter Printing Section
##########################################
# letter dates
dragons_date = "March 17, 1pm"
sharks_date = "March 17, 3pm"
raptors_date = "March 18, 1pm"
# the letter we are sending to parents asci art extracredit.
letter_to_parent = """
Dear {},
Your child, {} has been assigned to Team {}.  The first practice is scheduled for {}.
We look forward to seeing your child there!

Sincerely,
Coach Betker

 ___  ___   ___ ___ ___ _ __
/ __|/ _ \ / __/ __/ _ \ '__|
\__ \ (_) | (_| (_|  __/ |
|___/\___/ \___\___\___|_|

"""
# function defines names for letter .txt files.
def filenamer(name,team):

    name = name.replace(" ", "_")
    name = team +"/"+ name.lower()+".txt"
    return name

try:
    os.mkdir("sharks")
    os.mkdir("raptors")
    os.mkdir("dragons")
except:
    pass

# loop through each team and write the letters to folders.
for player in dragons:
    f = open(filenamer(player[0],"dragons"), 'w')
    f.write(letter_to_parent.format(player[3],player[0],"Dragons", dragons_date))
    f.close()

for player in sharks:
    f = open(filenamer(player[0],"sharks"), 'w')
    f.write(letter_to_parent.format(player[3],player[0],"Dragons", dragons_date))
    f.close()

for player in raptors:
    f = open(filenamer(player[0],"raptors"), 'w')
    f.write(letter_to_parent.format(player[3],player[0],"Dragons", dragons_date))
    f.close()


# print(dragons)
# print(len(sharks))
# print(len(raptors))
# print(letter_to_parent)


