#Overwatch 2 "SR" caluclator. 
#With the new ranking system of Overwatch 2, there are no raw numbers to use, but ranks and divisions. 
#This script serves to take player rank and division as input and find the "average" rank of the players to find a scrimmage match with.
#Early iteration of this script will allow for 5 player inputs, however later revisions will allow for x player inputs.
#This script will eventually move into a web application based focus with the new learning of node js, for now it will be a standalone app. 
import time 

#This serves to create a dictionary for arbitrary player values ranging from 10-70 depending on rank. This also creates a blank list to store player input data. 
ranks = {"BRONZE": 10, "SILVER": 20, "GOLD": 30, "PLATINUM": 40, "DIAMOND": 50, "MASTERS": 60, "GRANDMASTERS": 70}
formRank = []

#This function takes user input for a users rank, checks to see it is valid, formats the data, and stores the data in the formRank list for use later.
def player_input():
    x = 1
    while x <= 5:
        try:
            rawRank = input("Please enter player {}'s Overwatch 2 rank: ".format(x))
            rank, division = rawRank.split(' ', 1)
            rank = rank.upper()
            numRank = ranks[rank]
            division = int(division)
            if 0 < division <= 5:
                pass
            else:
                raise Exception
            rawFormNum = numRank + (5/division)
            formRank.append(rawFormNum)
            x = x+1
        except:
            print("invalid input. please try again.")

#The function calculates the average ranking of the team along with some logical math for situations where a teams average division is higher than or equal to 5.
def calculate_final():
    global finalDivision
    global finalRank
    teamAverageRaw = round(sum(formRank)/len(formRank))
    n = [int(a) for a in str(teamAverageRaw)]
    numRank = ((n[0]*10))
    finalDivision = round(n[1])
    if finalDivision >= 5:
        finalDivision = 1
    finalRank = (list(ranks.keys())[list(ranks.values()).index(numRank)])
    return finalDivision, finalRank

#This sections prints the welcome message, calls our functions, and outputs the results of the script running.
print("Welcome to the Overwatch 2 Average Rank calculator!\nValid input for ranks include:\nBronze\nSilver\nGold\nPlatinum\nDiamond\nMasters\nGrandmasters\nPlease input the rank and division such as: Silver 1.")
player_input()
calculate_final()
print("Search for a scrim with the average team rank: "+ (((finalRank).lower()).capitalize()) +" "+ str(finalDivision))
print("This program will auto exit in 10 seconds....")
time.sleep(10)