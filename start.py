# import CSV
# Sort in dictionary - order by height
# send every third person to a team.
# Color Code RTF document for

#Sort list into YES or NO - Then sort by height.
from operator import itemgetter
rookieslist = []
veteranslist = []



import csv
with open('soccer_players.csv', newline='') as players:
        teamplayers = csv.reader(players, delimiter=',', quotechar='|')

        for player in teamplayers:
            if player[2] == "YES":
                veteranslist.append(player)
            elif player[2] == "NO":
                rookieslist.append(player)


vetlist = sorted(veteranslist, key=itemgetter(1), reverse=True)
rooklist = sorted(rookieslist, key=itemgetter(1), reverse=True)
rank_sort = vetlist + rooklist

dragons = rank_sort[0::3]
sharks = rank_sort[1::3]
raptors = rank_sort[2::3]
###########################################
# Letter Printing Section
##########################################

letter_to_parent = """

Dear {},
Your child, {} has been assigned to Team {}.  The first practice is scheduled for {}.
We look forward to seeing your child there!




                           ,;;;:.
                          ;;''''`:
                          ;(  O O|              ,;;,
                           |   _\|              \  |
                            \__-/              ,' /
                            |   |             /  /
                      _,--''`---'''-------.,-'  /
                    ,'  /          `.     |  _,'
                  ,'    |====== WM =|     |-'
                 \      ,======|  |=|''---'
                / `.  ,' \      \/ /
              ,'. ,'`'   | --._    |
            ,'  ,'       |         |
        __,' _,'         \    -._  |
       `- ,-'            |---------)
      ';;'               ;:::::::::|
                        ;:::::::::::\
                       /::::::;:::::|
                      /_:::::/\:::::_\
                      / `-:_/  \,-' |
                     /    /     \   |
                     |   |      | _,)
                     \_,-\      |   |
                      \   |     |   |
                       |__|      \,-|
                       /##|      |  |
                      \##/       |  |
                     ,-'''-.     |,-|
                    // \_/ \\    `.##\
                    |\_/ \_/|      `--`
                    \/ \_/ \/
                     `-...-'
 ___  ___   ___ ___ ___ _ __
/ __|/ _ \ / __/ __/ _ \ '__|
\__ \ (_) | (_| (_|  __/ |
|___/\___/ \___\___\___|_|


"""




print(len(dragons))
print(len(sharks))
print(len(raptors))
print(letter_to_parent)


