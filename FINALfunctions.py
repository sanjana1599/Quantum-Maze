i6mport random
import pyqrcode
import webbrowser


def orderChange(n, list):
    #To change the order of list when any person enters gb stage &
    # Next turn has to be the next person in the order
    if n == 0:
        list = [1,2,3,0]
    elif n == 1:
        list = [2,3,0,1]
    elif n == 2:
        list = [3,0,1,2]
    elif n == 3:
        list = [0,1,2,3]
    list1 = list

    return list1

def name(playerName):
    # This returns the number which corresponds to the name of the player
   if playerName == "Mike" or playerName == "mike" or playerName == "m" or playerName == "M":
       n = 1
   elif playerName == "Beth" or playerName == "beth" or playerName == "b" or playerName == "B":
       n = 0
   elif playerName == "Emily" or playerName == "emily" or playerName == "e" or playerName == "E":
       n = 2
   elif playerName == "Kevin" or playerName == "kevin" or playerName == "k" or playerName == "K":
       n = 3

   return n

def pickUp(playerList1, deckList):
    # For picking up 2 cards each turn from deck, parameters are player's cardlist & deck
   playerList1.extend([deckList[0], deckList[1]])  # This appends two cards from deck to player list
   del deckList[0:2]  # It removes cards from the deck which have been added to the player list

   PlayerList = playerList1  # Putting them into new variables as one cannot return the same values as the parameters
   DeckList = deckList

   return PlayerList, DeckList

def specificCards(playerList1, mainList):
    # Creating a new list of cards allowed to TRADE, or to be played for ACTION
    # playerList1 is the original card list & mainList is either the original trade cardlist or action cardlist,
    # whichever we want to seperate
    newPlayerList1 = []
    for a in playerList1:  # Traversing through the player's list
        if a in mainList:  # Checking if any of the elements are in the mainList i.e. action or trade
            newPlayerList1.append(a)  # If so, then adding them to the new list created
    for b in newPlayerList1:  # Traversing through the new list
        if b in playerList1:  # If any of the cards are in the original card list
            playerList1.remove(b)  # Removing those cards to create seperate trade card list and remaining card list
    newPlayerList2 = playerList1

    return newPlayerList1, newPlayerList2

def updateCards(playerList1, newPlayerList1):
    # Used to concatenate trade/action card list back with original list
    newList1 = playerList1 + newPlayerList1

    return newList1  # Returns the combined list

def putActionBack(playerList1, num, deckList):
    # Used to put the action card used back into the deck
    # playerList1 is the player's list, num is serial number of the action card used and deckList is main deck
    deckList.append(playerList1[num])
    playerList1.remove(playerList1[num])
    playerList2 = playerList1  # Creating new variables because returning the same values as parameters is problematic
    deckList1 = deckList

    return playerList2, deckList1

def trade(playerList1, playerList2, num1, num2):
    # Function for trade
    # playerList1 and playerList2 are card lists of players who are trading the cards;
    # num1 and num2 are serial numbers of the cards getting traded
    playerList1.append(playerList2[num2])
    playerList2.append(playerList1[num1])
    playerList1.remove(playerList1[num1])
    playerList2.remove(playerList2[num2])
    newList1 = playerList1
    newList2 = playerList2

    return newList1, newList2

def blindDraw(playerList1, playerList2):
    # Function for action card of blind draw
    # One random card is drawn from the list of the player chosen
    # Parameters: the player's list who plays the blind draw card and list of the player they want to play the card on
    n = random.randint(0,len(playerList2)-1)
    playerList1.append(playerList2[n])
    playerList2.remove(playerList2[n])
    newList1 = playerList1
    newList2 = playerList2

    return newList1, newList2

def forcedDraw(playerList1, playerList2, num):
    # playerList1 is cardlist of the person playing
    # playerList2 is the list of the player they are taking it from
    playerList1.append(playerList2[num])  # Num is the serial number of the card they wish to take
    playerList2.remove(playerList2[num])
    newList1 = playerList1
    newList2 = playerList2

    return newList1, newList2

def unconsiousUpdate(playerName, playersList):
    # Update Unconscious back to null through this
    # playerName means that this person might have played the unconscious card on anyone,
    # during their chance it should get nullified
    # playersList stores all the unconscious variables
   if playersList[0] == playerName:
       playersList[0] = ""
   elif playersList[1] == playerName:
       playersList[1] = ""
   elif playersList[2] == playerName:
       playersList[2] = ""
   if playersList[3] == playerName:
       playersList[3] = ""

   return playersList

def surrender(playerList1, playerList2,num3):
    # Used for the action card: surrender
    # Parameters: the player's list who plays the surrender card and the list of the player they want to give the card to
   playerList2.append(playerList1[num3])
   playerList1.remove(playerList1[num3])
   newList1 = playerList1
   newList2 = playerList2

   return newList1, newList2

def checkAction(playerList1, mainList):
    # Function to check whether the person has any action cards, used when someone says that,
    # They have collected all 5 reality cards
    # playerList1 is the player's list of card, mainList is the list of action cards
   for x in playerList1:
       if x in mainList:
           output = False
       else:
           output = True

   return output

def realityCheck(playerList, reality):
    # To check whether the player has collected all reality cards from their reality
    count = 0  # To keep a count of the reality cards they have
    for x in range(len(playerList)):
        if reality in playerList[x]:
            count = count + 1
    if count == 5:
        output = True
    else:
        output = False

    return output

def gbCards(playerList1, playerReality, deckList):
    # Separating gamebreaker player's reality cards, and putting other reality extra cards back in the deck
   playerListGB = []
   playerListExtra = []
   for a in playerList1:
       if playerReality in a:
           playerListGB.append(a)
       else:
           playerListExtra.append(a)
   deckList = playerListExtra + deckList
   random.shuffle(deckList)

   return playerListGB, deckList

def diceProbability(num, count):
    # To check whether they have won during the dice roll in the gamebreaker stage
   if count == 1:  # Count represents the number of people in the gamebreaker stage
     if 8 <= num <= 12:
         output = True
     else:
         output = False

   elif count == 2:
       if 9 <= num <= 12:
           output = True
       else:
           output = False

   elif count == 3:
       if 10 <= num <= 12:
           output = True
       else:
           output = False

   elif count == 4:
       if 11 <= num <= 12:
           output = True
       else:
           output = False

   return output


def updateHTML(playerTrade, playerAction, playerName, playerReality, action, playerName2):
    # Updating html pages after each action
   f1 = open(playerName + ".html", "w")
   html = "<html>"  # Create the data to write to the html file
   html += "<style> h1 { font-size: 60px; } h2 { font-size: 50px; } h4 { font-size: 30px; }" \
           " h5 { font-size: 20px; } p { font-size: 35px; } </style>"
   # Specifying font size
   html += "<h1>" + playerName + "</h1><br>"
   html += "<h2>Reality: " + playerReality + "</h2><br>"
   html += "<h4>THESE ARE YOUR CARDS:</h4>"
   html += "<h4>Trade Cards</h4>"
   if not action:
       pass
   else:
       html += "<h4>" + playerName2 + " played the " + action + " card on you</h4>"
       if action == "blind draw":
           html += "<h5>Someone has sneaked into your cardlist, watch out!</h5>"
       elif action == "surrender":
           html += "<h5>Hands up, its time to accept what your fate brings you</h5>"
       elif action == "forced draw":
           html += "<h5> Hiding your cards won't help anymore, give up what" + playerName + " demands </h5>"
       elif action == "snooze":
           html += "<h5> Zzzzzz time to take a nap Zzzzzz </h5>"
       elif action == "unconscious":
           html += "<h5> Too bad you got knocked out, go take rest</h5>"
       html += "<br>"

   x = len(playerTrade)
   if x%2 == 0:
       y = x
   else:
       y = x-1
   for j in range(0,y,2):
       # Displaying Trade Card images two at a time and serial numbers in tabular format
       html +="<img src='images/" + playerTrade[j] \
              +".jpg' style=' float: left; width: 300px; margin-right: 1%; margin-bottom: 0.5em;'>"
       html += "<img src='images/" + playerTrade[j+1] \
               + ".jpg' style=' float: left; width: 300px; margin-right: 1%; margin-bottom: 0.5em;'>"
       html += '<p style="clear: both;">'
       html += "<table style = 'width:600px'><tr><th>"+str(j+1)+"</th><th>"+str(j+2)+"</th></tr></table>"
   if x%2!= 0:
       # For odd number of images to display
       html +="<img src='images/" + playerTrade[x-1] \
              +".jpg' style=' float: left; width: 300px; margin-right: 1%; margin-bottom: 0.5em;'>"
       html += "<h3 style = 'margin-left: 140px; margin-top: 485px'>"+str(x)+"<h3>"
   html += "<br>"
   html += "<h4>Action Cards</h4>"
   z = len(playerAction)
   if z % 2 == 0:
       q = z
   else:
       q = z - 1
   for k in range(0, q, 2):
       # Displaying Action Card images two at a time and serial numbers in tabular format
       html += "<img src='images/" + playerAction[k] \
               + ".jpg' style=' float: left; width: 300px; margin-right: 1%; margin-bottom: 0.5em;'>"
       html += "<img src='images/" + playerAction[k + 1] \
               + ".jpg' style=' float: left; width: 300px; margin-right: 1%; margin-bottom: 0.5em;'>"
       html += '<p style="clear: both;">'
       html += "<table style = 'width:600px'><tr><th>" \
               + str(k + 1) + "</th><th>" + str(k + 2) + "</th></tr></table>"
   if z % 2!= 0:
       # For odd number of images to display
       html += "<img src='images/" \
               + playerAction[z - 1] + ".jpg' style=' float: left; width: 300px; margin-right: 1%; margin-bottom: 0.5em;'>"
       html += "<h3 style = 'margin-left: 140px; margin-top: 485px'>" + str(z) + "<h3>"


   f1.write(html)
   f1.close()


def showHTML(StoryList, playerName):
    # Displaying story cards and creating qr code for player webpages
    f2 = open(playerName + ".html", "w")
    html = "<html>"
    html += "<img src='images/" + StoryList[0] \
            + ".jpg' style=' float: left; width: 300px; margin-right: 1%; margin-bottom: 0.5em;'>"
    html += "<img src='images/" + StoryList[1] \
            + ".jpg' style=' float: left; width: 300px; margin-right: 1%; margin-bottom: 0.5em;'>"
    html += '<p style="clear: both;">'
    f2.write(html)
    f2.close()
    url_html = "http://192.168.43.213:7800/" + playerName + ".html"

    qr = pyqrcode.create(url_html)  # Creates QR code of url_html

    qr.svg(playerName + "-url.svg", scale=8)  # Save the QR Code as an svg

    url_qr = "http://localhost:7800/" + playerName + "-url.svg"
    # Upload the URL to the local host using the IPV4 of the laptop

    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application %s"

    webbrowser.open_new(url_qr)


def storyHTML(StoryList, playerName1, num):
    # Displaying story cards
    f2 = open(playerName1 + ".html", "w")
    html = "<html>"
    for i in range(0,num,2):
        html += "<img src='images/" + StoryList[i] \
                 + ".jpg' style=' float: left; width: 300px; margin-right: 1%; margin-bottom: 0.5em;'>"
        html += "<img src='images/" + StoryList[i+1] \
                + ".jpg' style=' float: left; width: 300px; margin-right: 1%; margin-bottom: 0.5em;'>"
        html += '<p style="clear: both;">'
    f2.write(html)
    f2.close()

def gameBreakerPrint(playerName, gbCount, e, ordergb):
    # Printing probabilities based on number of players in gamebreaker stage
    f1 = open(playerName + ".html", "w")
    html = "<html>"  # Create the data to write to the html file
    html += "<style> h1 { font-size: 80px; } h2 { font-size: 70px; } h3 { font-size: 30px; } h4 { font-size: 40px; }" \
            " h5 { font-size: 40px; } p { font-size: 35px; } </style>" # Specifying font size
    html += "<h4>"+playerName + "'s turn to roll.</h4>"
    if gbCount == 1:
        html += "<h3>This is the GameBreaker Stage, and you are the first to get here!</h3>"
        html += "<h3>Roll the dice to get a total of 8 or higher to win the game.</h3><br>"
    if gbCount == 2:
        html += "<h3>This is the GameBreaker Stage, and now there are two of you.</h3>"
        html += "<h3>Roll the dice to get a total of 9 or higher to win the game.</h3><br>"
    if gbCount == 3:
        html += "<h3>This is the GameBreaker Stage.</h3>"
        html += "<h3>Three of you are contenders for the victory, roll to get a total of 10 or higher to win the game.</h3><br>"
    if gbCount == 4:
        html += "<h3>All four of you are in the GameBreaker Stage with no victory yet.</h3>"
        html += "<h3>You must roll a total of 11 or 12 to win the game.</h3><br>"

    html += "<h4>Hit enter to roll the dice and determine your fate.</h4>"

    f1.write(html)
    f1.close()
    inp5 = input("Refresh your page and then press enter to determine your fate.")
    outputfinal, ordergb2 = gameBreakerStage(playerName, e, ordergb, gbCount)
    print("Refresh again to see what happened")

    return outputfinal, ordergb2


def gameBreakerStage(playerName, e, ordergb, countgb):
    # Rolling dice and returning win or lose output
    f1 = open(playerName + ".html", "w")
    html = "<html>"  # Create the data to write to the html file
    html += "<style> h1 { font-size: 60px; } h2 { font-size: 50px; } h3 { font-size: 45px; } h4 { font-size: 40px; }" \
            " h5 { font-size: 35px; } p { font-size: 35px; } </style>" # Specifying font size
    ordergb3 = []
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    html += "<h1>" + playerName + "</h1><br>"
    html += "<h4>The numbers you rolled are " + str(n1) + " and " + str(n2) + ".</h4><br>"
    addition = n1 + n2
    outputfinal1 = diceProbability(addition, countgb)

    if outputfinal1 is True:
        html += "<h4>"+playerName + ", you rolled a total of " + str(addition) + "!</h4>"
        html += "<h4>Congratulations, you have successfully escaped the Quantum Maze!</h4><br>"
        html += "<h2>GAME OVER</h2>"
    else:
        html += "<h4>"+playerName + ", you rolled a total of " + str(addition) + ".</h4>"
        html += "<h4>Loser, you're still in the game.</h4>"
        html += "<h5>Another reality, another house. Try again next turn.</h5><br>"
        ordergb1 = orderChange(e, ordergb)
        ordergb3 = ordergb1
    f1.write(html)
    f1.close()

    return outputfinal1, ordergb3
