import random
import sys

suits = ("H", "D", "S", "C")
ranks = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2" )

def main():

  print("Hello, let's start the WAR game")
  name1, name2 = get_player_names()
  start_the_game(name1, name2)


#create a single card
class Card:

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return f"{self.rank}{self.suit}"


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
    return self.all_cards.pop()


#create a player with no cards, that removes and adds up the cards
class Player:
  def __init__(self): 
    self.name = input("Enter the name of the player: ")     
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

#### GAME LOGIC ####

# Add the players
def get_player_names():
  player1 = Player()
  player2 = Player()
  #player1 = input("Enter the name of the first player: ")
  #player2 = input("Enter the name of the second player: ")
  return (player1, player2)

def start_the_game(name1, name2):

  # introduce the players
  player_one = name1
  player_two = name2

  # create and shuffle the deck
  new_deck = Deck()
  new_deck.shuffle()

  # split the deck between players
  for i in range(len(new_deck.all_cards)//2):
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
      print(f"{player_two.name} is out of cards")
      print(f"{player_one.name} is the winner!")
      print("GAME OVER")
      sys.exit()

    #else game continues 
    print(f"{round} round:") 
    player_one_cards = []
    player_one_cards.append(player_one.remove_card())
    
    #create_game
    player_two_cards = []
    player_two_cards.append(player_two.remove_card())
   
    war = True

    while war:
      if ranks.index(player_one_cards[-1].rank) < ranks.index(player_two_cards[-1].rank):
        player_one.add_cards(player_one_cards)
        player_one.add_cards(player_two_cards)
        print(f"{player_one.name} wins the round")
        war = False
      
      elif ranks.index(player_one_cards[-1].rank) > ranks.index(player_two_cards[-1].rank):
        player_two.add_cards(player_one_cards)
        player_two.add_cards(player_two_cards)
        print(f"{player_two.name} wins the round")
        war = False
      
      #if cards are equal:
      else:
        print("War!")

        #check if players are able to play war
        if len(player_one.player_cards) < 5:
          game = False
          print(f"{player_one.name} cannot go into the war.")
          print(f"{player_two.name} wins!")
          print("Game Over")
          break
        
        elif len(player_two.player_cards) < 5:
          game = False
          print(f"{player_two.name} cannot go into the war.")
          print(f"{player_one.name} wins!")
          print("Game Over")
          break

        else:
          for num in range(5):
            player_one_cards.append(player_one.remove_card())
            player_two_cards.append(player_two.remove_card())
  
if __name__ == "__main__":
  main()

  

