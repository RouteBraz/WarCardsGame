import random
suits = ("H", "D", "S", "C")
ranks = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2" )

#create a single card
class Card:

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return f'{self.suit}{self.rank}'

#####################
### REMOVE at the end
#card1 = Card("S", "A")
#print(card1)

#create a deck of cards with possibility to shuffle
class Deck:
  def __init__ (self): 
    self.all_cards = []

    for suit in suits: 
      for rank in ranks: 
        self.all_cards.append(Card(suit, rank))

  def shuffle(self): 
    random.shuffle (self.all_cards)

#create a player, that removes and adds up the cards
class Player:
  def __init__(self, name): 
    self.name = name 
    self.all_cards = []

  def remove_card(self):
    return self.all_cards.pop(0)
  
  def add_cards(self, new_cards):
    if type(new_cards) == type ([]):
      self.all_cards.extend(new_cards)
    else: 
      self.all_cards.append(new_cards)

  def __str__(self): 
    return f'{self.name} has {len(self.all_cards)} cards'

### REMOVE at the end ########
##############################  
#gamer = Player("Mario")
#print(gamer)

      

  

