from random import randint

playerNameOne=input("What is player your name?")

def cardDeck():
  deck= ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K','A']
  cardType=['Hearts','Spades','Clubs','Diamonds']
  hand=[]
  for i in cardType:
    for x in deck:
      deck.append(x+' of '+i)
  return deck

def newCard(deck):
  return deck[randint(0,len(deck)-1)]
  
def removeCard(deck,card):
  


def playerOne():
  cardOne