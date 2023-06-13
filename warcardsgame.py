import random
import sys

def main():

  suits = ("H", "D", "S", "C")
  ranks = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2" )

   print("Hello, let's start the WAR game")
   get_player_names()
   start_the_game(name1, name2)




#create a single card
class Card:

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return f'{self.suit}{self.rank}'

#####################
### REMOVE at the end
# card1 = Card("S", "A")
# print(card1) AH

# create a deck of cards with possibility to shuffle
class Deck:
  def __init__ (self): 
    self.all_cards = []

    for suit in suits: 
      for rank in ranks: 
        self.all_cards.append(Card(suit, rank))

# shuffle cards
  def shuffle(self): 
    random.shuffle (self.all_cards)

# remove one card from the list of all cards  
  def deal_card(self):
        return self.cards.pop()


#create a player with no cards, that removes and adds up the cards
class Player:
  def __init__(self, name): 
    self.name = name     
    self.player_cards = []

  #remove one card from the list of player_cards from the top of the deck
  def remove_card(self):
    return self.player_cards.pop(0)
  
  def add_cards(self, new_cards):
    if type(new_cards) == type ([]):
      self.player_cards.extend(new_cards)
    else: 
      self.player_cards.append(new_cards)

  def __str__(self): 
    return f'{self.name} has {len(self.player_cards)} cards'

### REMOVE at the end ########
##############################  
#gamer = Player("Mario")
#print(gamer)

#### GAME LOGIC ####

# Add the players
def get_player_names():
  player1 = input("Enter the name of the first player: ")
  player2 = input("Enter the name of the second player: ")
  return player1, player2

def start_the_game(name1, name2):

  # introduce the players
  player_one = Player(name1)
  player_two = Player(name2)


  # create and shuffle the deck
  new_deck = Deck()
  new_deck.shuffle()


  # split the deck between players
  for i in range(len(new_deck.all_cards)/2):
    player_one.add_cards(new_deck.deal_card())
    player_two.add_cards(new_deck.deal_card())

  # start the game
  game = True

  round = 0

  while game:
    round += 1
     
  # check the cards number of each player
  # announce the winner if any doesn't have cards
  if len(player_one.all_cards) == 0:
    game = False
    print(f"{player_one.name} is out of cards")
    print(f"{player_two.name} is the winner!")
    print("GAME OVER")
    sys.exit()

  elif len(player_two.all_cards) == 0:
    game = False
    print(f"{player_two.name} is out of cards")
    print(f"{player_one.name} is the winner!")
    print("GAME OVER")
    sys.exit()

  #else game continues  
  else:
    print(f"{round} round:")

    card1 = player1.player_card.pop()
    card2 = player2.player_card.pop()

    print(f"{player_one.name} plays: {card1}")
    print(f"{player_two.name} plays: {card2}")

    if ranks.index(card1.rank) < ranks.index(card2.rank):
      player_one.add_cards(card1, card2)
      print(f"{player_one.name} wins the round")
    
    elif ranks.index(card1.rank) > ranks.index(card2.rank):
      player_two.add_cards(card1, card2)
      print(f"{player_two.name} wins the round")




  


  # if both cards are equal, announce the war


  # if not war, remove card from loser, add to the winner, announce the winner and print both player cards

if __name__ == "__main__":
  main()

  

