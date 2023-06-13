import random
import sys

def main():

  suits = ("H", "D", "S", "C")
  ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2" ] # changed to list to work as tuple of strings to work with add_cards method argument
  print("Hello, let's start the WAR game")
  name1, name2 = get_player_names()  # assigned name1/2
  start_the_game(name1, name2, suits, ranks)   # added suits/ranks arguments

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

  def __init__ (self, suits, ranks):   #indentation changed
    self.all_cards = []

    for suit in suits: 
      for rank in ranks: 
        self.all_cards.append(Card(suit, rank))

# shuffle cards
  def shuffle(self): 
    random.shuffle (self.all_cards)

# remove one card from the list of all cards  
  def deal_card(self):
    return self.all_cards.pop()     #indentation changed


#create a player with no cards, that removes and adds up the cards
class Player:
  def __init__(self, name): 
    self.name = name     
    self.player_cards = []

  #remove one card from the list of player_cards from the top of the deck
  def remove_card(self):
    return self.player_cards.pop(0)
  
  def add_cards(self, *new_cards):  # changed argument to include additional, card 1 & card 2 args
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

def start_the_game(name1, name2, suits, ranks):  # added suits/ranks arguments

  # introduce the players
  player_one = Player(name1)
  player_two = Player(name2)


  # create and shuffle the deck
  new_deck = Deck(suits, ranks) # added args
  new_deck.shuffle()


  # split the deck between players
  for i in range(len(new_deck.all_cards)//2):  # changed operator to // as error given regarxding float
    player_one.add_cards(new_deck.deal_card())
    player_two.add_cards(new_deck.deal_card())

  # start the game
  game = True

  round = 0

  while game:
    round += 1
     
    # check the cards number of each player
    # announce the winner if any doesn't have cards
    if len(player_one.player_cards) == 0:
      game = False
      print(f"{player_one.name} is out of cards")
      print(f"{player_two.name} is the winner!")
      print("GAME OVER")
      sys.exit()

    elif len(player_two.player_cards) == 0:
      game = False
      print(f"{player_two.name} is out of cards")                   # Fixed indentation within while loop
      print(f"{player_one.name} is the winner!")
      print("GAME OVER")
      sys.exit()

    #else game continues  
    else:
      print(f"{round} round:")

      card1 = player_one.player_cards.pop()   # changed from player1 to player_one
      card2 = player_two.player_cards.pop()    # same change for player 2

      print(f"{player_one.name} plays: {card1}")
      print(f"{player_two.name} plays: {card2}")

      if ranks.index(card1.rank) < ranks.index(card2.rank):
        player_one.add_cards(card1, card2)
        print(f"{player_one.name} wins the round")
      
      elif ranks.index(card1.rank) > ranks.index(card2.rank):
        player_two.add_cards(card1, card2)
        print(f"{player_two.name} wins the round")

# implemented war option if tie
    # if both cards are equal, announce the war
      else:
        # add 3 cards form each palyer to war_cards list
        war_cards = []
        for _ in range(3):
          war_cards.append(player_one.remove_card())
          war_cards.append(player_two.remove_card())

        # continue by playing card from each player
        war_card1 = player_one.remove_card()
        war_card2 = player_two.remove_card()

        print(f"{player_one.name} plays: {war_card1}")
        print(f"{player_two.name} plays: {war_card2}")

        if ranks.index(war_card1.rank) < ranks.index(war_card2.rank):
          player_one.add_cards(war_cards + [card1, card2, war_card1, war_card2])
          print(f"{player_one.name} wins the war")
        elif ranks.index(war_card1.rank) > ranks.index(war_card2.rank):
          player_two.add_cards(war_cards + [card1, card2, war_card1, war_card2])
          print(f"{player_two.name} wins the war")
        else:
          # If there is another war, add the cards to the war_cards list and continue the loop
          war_cards.extend([card1, card2, war_card1, war_card2])



'''
Still a few things to do for the changes i made to actually work, 
will update branch after finishing current prohjects i am working on
'''




  # if not war, remove card from loser, add to the winner, announce the winner and print both player cards

if __name__ == "__main__":
  main()

  

