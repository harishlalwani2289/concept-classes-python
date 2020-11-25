harishCards = "10 11 31"
pratikshaCards = "4 2 29"
player1 = "24 26 45"
player2 = "22 44 28"
player3 = "18 "
player4 = ""

harishCards = [int(i) for i in harishCards.split()]
pratikshaCards = [int(i) for i in pratikshaCards.split()]
player1 = [int(i) for i in player1.split()]
player2 = [int(i) for i in player2.split()]
player3 = [int(i) for i in player3.split()]
player4 = [int(i) for i in player4.split()]

hukum = list(range(13))
chidi = list(range(13, 26))
hearts = list(range(26, 39))
diamond = list(range(39, 52))


def findTheCardLabel(card):
    if card % 13 == 9:
        return "J"
    elif card % 13 == 10:
        return "Q"
    elif card % 13 == 11:
        return "K"
    elif card % 13 == 12:
        return "A"
    else:
        return card % 13 + 2


def printSet(mySet, name):
    for card in mySet:
        print(card[0], card[1], end=" ")
    print(name)


def getTheCards(cards, name):
    mySet = []
    for card in cards:
        label = findTheCardLabel(card)
        if card in hukum:
            mySet.append(("\u2664", label))
        elif card in hearts:
            mySet.append(("\u2661", label))
        elif card in chidi:
            mySet.append(("\u2663", label))
        elif card in diamond:
            mySet.append(("\u2662", label))

    printSet(mySet, name)


getTheCards(harishCards, "Harish")

if len(pratikshaCards) != 0:
    getTheCards(pratikshaCards, "Pratiksha")

if len(player1) != 0:
    getTheCards(player1, "Player1")

if len(player2) != 0:
    getTheCards(player2, "Player2")

if len(player3) != 0:
    getTheCards(player3, "Player3")

if len(player4) != 0:
    getTheCards(player4, "Player4")

# print("Winner", patti_winner.findWinner(list((player1, player2,
#                                               player3, player4,
#                                    harishCards, pratikshaCards))))
