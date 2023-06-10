import random
suits = ("H", "D", "S", "C")
ranks = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2" )

class Card:

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return f'{self.rank} of {self.suit}'

suits[2]


