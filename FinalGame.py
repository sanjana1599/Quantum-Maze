import random
import pickle
import FINALfunctions as quantfunc  # Functions are in a different file called QuantumMazeFunctionsCopy

pickleIn = open("tradePickle", "rb")
tradeList = pickle.load(pickleIn) # list of trade cards

pickleIn = open("actionPickle", "rb")
actionList = pickle.load(pickleIn) # list of action cards

storyList = ["Story Card 1", "Story Card 2", "Story Card 3", "Story Card 4",
            "Story Card 5", "Story Card 6"]

realityList = ["Wine Glass", "Wall Clock", "Photo Frame", "Black Hat",
              "Candlestick", "Phone Book"]  # List of the reality cards

deck = tradeList + actionList  # The main deck has both trade cards and action cards
random.shuffle(deck)  # Function to shuffle the deck
random.shuffle(realityList)  # Function to shuffle the realities


class playerClass:  # A class to create all the variables needed for the object
    def __init__(self):
        self.cardList = [] # Each player's cards
        self.reality = "" # Each player's reality
        self.snooze = 0  # The value of this variable changes to 1 when someone plays a snooze card on you
        self.name = "" # Player's name
        self.tradeCards = [] # Player's trade cards
        self.actionCards = [] #p Player's action cards
        self.unconscious = ""  # The value of unconscious to the person who will play the unconscious card on you
        self.gameBreaker = False # Stores value of whether player is in Gamebreaker Stage
        self.round = 0  # to mark each players second round for pick up
        self.counterAction = 0


player = []  # Creating a list to store all the objects that will be created
for i in range(4):  # Loop is run 4 times because 4 objects need to be created for the 4 players
    player.append(playerClass())  # creating objects of the class made above and adding those objects into the list
    player[i].reality = realityList[i]  # Assigning the reality card to each object i.e. each player

k = 0  # Variable used to deal the cards in the beginning of game
for i in range(3):  # range is 3 because 3 cards need to be dealt in the beginning
    for j in range(4):  # range is 4 because there are 4 players
        player[j].cardList.append(deck[k])  # Adding the cards from the deck to each player's list of cards
        k = k + 1

del deck[0:12]  # Deleting the cards from the deck that have been given to the players
player[0].name = "Beth"  # Assigning names to each player according to the characters of the movie
player[1].name = "Mike"
player[2].name = "Emily"
player[3].name = "Kevin"

output2 = False  # the value remains false until someone wins the game
un = []  # Making a list for the unconscious variables
         # because need to return 4 values in the unconsciousUpdate function
check = 0
# to check whether player has action cards or not
for i in range(4):
    un.append(player[i].unconscious)  # Appending the unconscious variables to the list

counter = 0  # To ensure that the person has trade cards

count1 = 0  # to keep a count of how many people have entered gamebreaker stage
order = [0, 1, 2, 3]  # 0 - Beth, 1 - Mike, 2 - Emily, 3 - Kevin
orderName = ["Mike", "Kevin", "Beth", "Emily", "m", "k", "b", "e", "mike", "kevin",
            "beth", "emily", "M", "K", "E", "B"] # List to store possible inputs by user for name
finalOutput = False

print("The characters stuck together are in this wrong reality are Beth, Mike, Emily and Kevin.")
print("Trade cards wisely and sabotage your opponents to escape the Quantum Maze.")
print("Welcome to Quantum Maze. You may begin.")

for f in range(4):
    # Calling trade and action cards of each player
    # Story cards shown in twos to each player
    player[f].tradeCards, player[f].actionCards = quantfunc.specificCards(player[f].cardList, tradeList)
    quantfunc.showHTML(storyList, player[f].name)
inp10 = input("Hit enter to see what happens next and refresh your webpage")
for i in range(4):
    quantfunc.storyHTML(storyList, player[i].name, 4)
inp11 = input("Hit enter to see what happens next and refresh your webpage")

for i in range(4):
    quantfunc.storyHTML(storyList, player[i].name, 6)
inp12 = input("You may proceed to the Quantum Maze now. Hit Enter and refresh your screen to see your cards.")

for i in range(4):
    # Calling HTML function to show players' cards
    quantfunc.updateHTML(player[i].tradeCards, player[i].actionCards,player[i].name,
                        player[i].reality,None, None)
while finalOutput is False:  # Will remain false until someone wins
    for i in order:  # For the 4 players' turn
        if player[i].gameBreaker is False:  # For players not in game breaker stage
            if player[i].snooze == 0:  # Means that the snooze Action Card has not been played on you
                print(player[i].name + "'s Turn")
                if player[i].round == 1:  # Check if second round, so can pick up 2 cards
                    player[i].cardList = quantfunc.updateCards(player[i].actionCards, player[i].tradeCards)
                    player[i].cardList, deck = quantfunc.pickUp(player[i].cardList,deck)
                    # Adding two cards from the deck in every round
                    player[i].tradeCards, player[i].actionCards = quantfunc.specificCards(player[i].cardList,
                                                                                         tradeList)
                    quantfunc.updateHTML(player[i].tradeCards, player[i].actionCards,
                                         player[i].name, player[i].reality,None, None)
                    player[i].counterAction = 0 #If 1, then person has only trade cards
                    player[i].counterTrade = 0 #If 1, then person has only action cards
                for j in range(2):  # Each player has 2 chances per turn
                    player[i].round = 1
                    # Becomes 1 after first turn, so for next round value is 1 to pick up cards
                    print(player[i].name + ", here are your cards.")
                    if j == 0:
                    # If player made Unconscious in first chance,
                    # the card should not get nullified in player's second chance
                        un = quantfunc.unconsiousUpdate(player[i].name,un)
                        # Updating the unconscious variable in case existing player played that card on anyone
                        counter = 0  # To ensure that it doesn't go into trade loop later
                    while True:
                    # To keep asking until right answer is given
                        print("Do you want to play a chance? Press 'y' or 'n")
                        inp = input()
                        if inp == 'y' or inp == 'Y' or inp == 'n' or inp == 'N':
                            break
                        else:
                            print("Wrong input.")
                    num4 = 0  # Making another variable to be accessed later outside the while loop
                    if inp == 'y' or inp == 'Y':
                        while True:
                            print("Do you want to TRADE or play an ACTION CARD?")
                            print("Press 't' for Trade, and 'a' for Action Card")
                            inp1 = input()
                            if inp1 == 't' or inp1 == 'T' or inp1 == 'a' or inp1 == 'A':
                                break
                            else:
                                print("Wrong input.")
                        if inp1 == 't' or inp1 == 'T':
                            a = 1  # A condition for it to go into while loop
                            while a == 1:
                            # the loop runs in case the player they want to trade with, is Unconscious
                                if not player[i].tradeCards:  # In case player doesn't have trade cards
                                    print("You do not have trade cards.")
                                    print("Type 'a' if you want to play an action card.")
                                    print("Type 'n' if you do not want to play a chance.")
                                    inp1 = input()
                                    counter = 1  # So that it does not go into trade loop again
                                    break
                                while True:
                                    print("Which player do you want to trade with? Type the player's name or initial.")
                                    inp2 = input()
                                    if inp2 in orderName: # orderName is list with possible user input variations
                                        break
                                    else:
                                        print("Wrong input.")
                                num = quantfunc.name(inp2)  # Returns number corresponding to name player entered
                                num4 = num
                                # Since num going to be used outside loop, it is added into another variable
                                if not player[num].tradeCards:  # if other player does not have trade cards
                                    print(player[num].name, ", you do not have cards to trade with " + player[i].name)
                                    counter = 1
                                    break
                                if not un[num] and player[num].gameBreaker is False:
                                # un[num] means that the player is not unconscious
                                    while True:
                                        try:
                                            print(player[i].name + ", these are the cards you can trade.")
                                            print("Type in the serial number of the trade card you wish to trade.")

                                            inp5 = int(input())
                                            if (inp5 - 1) < len(player[i].tradeCards):
                                                break
                                            else:
                                                print("Wrong input, this number is out of your card range.")
                                        except:
                                            print("Wrong input.")
                                    while True:
                                        try:
                                            print(player[num].name + ", these are the cards you can trade.")
                                            print("Type in the serial number of the trade card you wish to trade.")

                                            inp6 = int(input())
                                            if (inp6 - 1) < len(player[num].tradeCards):
                                                break
                                            else:
                                                print("Wrong Input, this number is out of your card range.")
                                        except:
                                            print("Wrong input.")
                                    break
                                else:
                                    print("You cannot trade with this person as they are unconscious.")

                            num = num4
                            if num in [0, 1, 2, 3] and (not un[num]) and counter == 0:
                                # TRADE happening
                                player[i].tradeCards, player[num].tradeCards = quantfunc.trade(player[i].tradeCards,
                                                                                               player[num].tradeCards,
                                                                                               inp5 - 1,
                                                                                               inp6 - 1)
                                # Calling trade function
                                # inp3 - 1 because serial number in list starts from 0
                                quantfunc.updateHTML(player[i].tradeCards, player[i].actionCards,
                                                     player[i].name, player[i].reality, None, None)
                                quantfunc.updateHTML(player[num].tradeCards, player[num].actionCards,
                                                     player[num].name, player[num].reality, None, None)
                                print("Refresh your screens to see your cards")
                            elif num != [0, 1, 2, 3] and counter == 0:
                                print("Wrong input.")
                        counter = 0
                        if inp1 == 'a' or inp1 == 'A':  #ACTION happening
                            if not player[i].actionCards:  # In case player doesn't have ACTION cards
                                print("You do not have action cards to play.")
                                player[i].counterAction = 1  # so that it does not go into action loop again
                            num2 = -1
                            # initialising the variable for later
                            if player[i].counterAction == 0:  # when player has action cards
                                while True:
                                    try:
                                        print(player[i].name + ", type in the serial number of the action card you wish to play.")
                                        inp3 = int(input())  # Which action card
                                        if (inp3 - 1) < len(player[i].actionCards):
                                            break
                                        else:
                                            print("Wrong input, this number is out of your card range.")
                                    except:
                                        print("Wrong input")
                                while True:
                                    print("Which player do you want to use this card on?")
                                    print("Type the player's name or their initial.")
                                    inp4 = input()
                                    if inp4 in orderName:
                                        break
                                    else:
                                        print("Wrong Input.")

                                num2 = quantfunc.name(inp4)  # Corresponding the name to a number

                            if player[num2].gameBreaker is False and player[i].counterAction == 0:
                                # Check if player you played action card on is not in gamebreaker stage
                                # Check if you have action cards
                                if player[i].actionCards[inp3 - 1] == "Snooze":
                                    print("All these confusing events are too much for " + player[
                                        num2].name + ", who has now gone to take a nap.")
                                    player[num2].snooze = 1
                                    # changing the snooze variable for player you used the action card on
                                    player[i].actionCards, deck = quantfunc.putActionBack(player[i].actionCards,
                                                                                          inp3 - 1,
                                                                                          deck)
                                    # putting the action card used back in the deck
                                    quantfunc.updateHTML(player[i].tradeCards, player[i].actionCards,
                                                         player[i].name, player[i].reality, None, None)
                                    quantfunc.updateHTML(player[num2].tradeCards, player[num2].actionCards,
                                                         player[num2].name, player[num2].reality, "snooze", player[i].name)
                                    print("Refresh your screens")

                                elif player[i].actionCards[inp3 - 1] == "Unconscious":
                                    print("A fight broke out between " + player[num2].name + " and you, and so " +
                                          player[num2].name + " has been rendered unconscious.")
                                    player[num2].snooze = 1
                                    # Player who is unconscious will have to be snoozed also
                                    un[num2] = player[i].name
                                    # The player on whom the card is played
                                    # their unconscious variable will store name of player who played the card
                                    # for eg: if Beth played unconscious card on Mike
                                    # Mike's unconscious variable i.e. player[1].unconscious = Beth
                                    player[i].actionCards, deck = quantfunc.putActionBack(player[i].actionCards,
                                                                                          inp3 - 1, deck)
                                    quantfunc.updateHTML(player[i].tradeCards, player[i].actionCards,
                                                         player[i].name, player[i].reality, None, None)
                                    quantfunc.updateHTML(player[num2].tradeCards, player[num2].actionCards,
                                                         player[num2].name, player[num2].reality, "unconscious",
                                                         player[i].name)
                                    print("Refresh your screens")

                                elif player[i].actionCards[inp3 - 1] == "Surrender":
                                    print("Dump a useless card on a player you don't like.")
                                    while True:
                                        try:
                                            print("Which trade card do you want to force onto another player?")
                                            print("Enter its serial number.")
                                            inp7 = int(input())
                                            if (inp7 - 1) < len(player[i].tradeCards):
                                                break
                                            else:
                                                print("Wrong input, this number is out of your card range.")
                                        except:
                                            print("Wrong input.")

                                    player[i].tradeCards, player[num2].tradeCards = quantfunc.surrender(player[i].tradeCards,
                                                                                                        player[num2].tradeCards,
                                                                                                        (inp7 - 1))
                                    # Calling the Surrender function
                                    player[i].actionCards, deck = quantfunc.putActionBack(player[i].actionCards,
                                                                                          inp3 - 1,
                                                                                          deck)
                                    # Putting the used action card back in the deck
                                    quantfunc.updateHTML(player[i].tradeCards, player[i].actionCards, player[i].name,
                                                         player[i].reality, None, None)
                                    quantfunc.updateHTML(player[num2].tradeCards, player[num2].actionCards,
                                                         player[num2].name, player[num2].reality, "surrender",
                                                         player[i].name)
                                    print("Refresh your screens")


                                elif player[i].actionCards[inp3 - 1] == "Forced Draw":
                                    print("Take any card you want from a player without having to give a card in return.")
                                    while True:
                                        print("Which trade card do you want to steal from another player?")
                                        try:
                                            print(player[num2].name, " enter its serial number.")

                                            inp7 = int(input())
                                            if (inp7 - 1) < len(player[num2].tradeCards):
                                                break
                                            else:
                                                print("Wrong input, this number is out of your card range.")
                                        except:
                                            print("Wrong input.")
                                    player[i].tradeCards, player[num2].tradeCards = quantfunc.forcedDraw(player[i].tradeCards,
                                                                                                         player[num2].tradeCards,
                                                                                                         (inp7 - 1))
                                    player[i].actionCards, deck = quantfunc.putActionBack(player[i].actionCards,
                                                                                          inp3 - 1,
                                                                                          deck)
                                    quantfunc.updateHTML(player[i].tradeCards, player[i].actionCards, player[i].name,
                                                         player[i].reality, None, None)
                                    quantfunc.updateHTML(player[num2].tradeCards, player[num2].actionCards,
                                                         player[num2].name, player[num2].reality, "forced draw",
                                                         player[i].name)
                                    print("Refresh your screens")
                                elif player[i].actionCards[inp3 - 1] == "Blind Draw":
                                    print("Try your luck at picking a random card from a player, hope its a card you want!")
                                    player[i].cardList = quantfunc.updateCards(player[i].tradeCards,
                                                                               player[i].actionCards)
                                    player[num2].cardList = quantfunc.updateCards(player[num2].tradeCards,
                                                                               player[num2].actionCards)
                                    player[i].cardList, player[num2].cardList = quantfunc.blindDraw(player[i].cardList,
                                                                                                    player[num2].cardList)
                                    # Calling blind draw function which returns updated cards of both players
                                    player[i].tradeCards, player[i].actionCards = quantfunc.specificCards(player[i].cardList,
                                                                                                          tradeList)
                                    player[num2].tradeCards, player[num2].actionCards = quantfunc.specificCards(player[num2].cardList,
                                                                                                                tradeList)
                                    player[i].actionCards, deck = quantfunc.putActionBack(player[i].actionCards,
                                                                                          inp3 - 1, deck)
                                    quantfunc.updateHTML(player[i].tradeCards, player[i].actionCards, player[i].name,
                                                         player[i].reality, None, None)
                                    quantfunc.updateHTML(player[num2].tradeCards, player[num2].actionCards,
                                                         player[num2].name, player[num2].reality, "blind draw",
                                                         player[i].name)
                                    print("Refresh your screens")

                                else:
                                    print("Wrong input.")

                            elif player[num2].gameBreaker is True:
                                print("You cannot play an action card on them as they are in the GameBreaker Stage.")
                        if inp1 == 'n' or inp1 == 'N':
                            print("Next player's turn")
                            break
                    else:
                        print("Have you collected all five of your Reality Cards? Say 'y' for yes and 'n' for no")
                        inp5 = input()
                        if inp5 == "yes" or inp5 == "Yes" or inp5 == "y" or inp5 =="Y":
                            output1 = quantfunc.realityCheck(player[i].tradeCards, player[i].reality)
                            # Check if they have all five cards of their reality
                            if not player[i].actionCards:
                                output2 = True
                            if output1 is True and output2 is True:
                                print("You are now in the GameBreaker Stage.")
                                player[i].cardList, deck = quantfunc.gbCards(player[i].cardList,
                                                                             player[i].reality,
                                                                             deck)
                                # Removing extra trade cards from player's list and adding to deck
                                global e
                                e = i
                                player[e].gameBreaker = True
                                count1 = count1 + 1  # To count how many players in Gamebreaker Stage
                                break
                            else:
                                player[i].tradeCards, player[i].actionCards = quantfunc.specificCards(player[i].cardList,
                                                                                                      tradeList)
                                print("You should have all 5 of your Reality cards and no Action Cards.")
                        else:  # if the player doesn't want to play a chance
                            print("Next player's turn")
                            break

                if player[i].gameBreaker is True: # Breaking out of these loops when reach Gamebreaker Stage
                    e = i
                    break
            else:
                print(player[i].name + ", you cannot play as you are taking a nap.")
                print("Next player's turn")
                player[i].snooze = 0
        elif player[i].gameBreaker is True:
            e = i
            break
    e = i #Gamebreaker Stage
    if player[e].gameBreaker is True:
        print("You are in the gameBreaker stage, Refresh your page.")
        finalOutput, order = quantfunc.gameBreakerPrint(player[e].name, count1, e, order)
        # Calling Gamebreaker function
        if finalOutput is True:
            break
        finalOutput = False
    if finalOutput is True:
        break # Game Over
    finalOutput = False
