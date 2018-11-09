#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.cards = [(rank, suite) for suite in SUITE for rank in range(13)]

    def shuffle(self):
        shuffle(self.cards)

    def cut(self):
        cards_in_hand = len(self.cards) // 2
        return (Hand(self.cards[:cards_in_hand]), Hand(self.cards[cards_in_hand:]))

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def remove(self):
        return self.cards.pop(0)

    def add(self, card):
        return self.cards.append(card)

    def __str__(self):
        return self.cards.__str__()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return "Player {name} with hand {hand}".format(name = self.name, hand = self.hand)


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
deck = Deck()
deck.shuffle()

def create_player(i, hand):
    return Player(input("Player {} name: ".format(i + 1)), hand)

players = [create_player(i, hand) for i, hand in enumerate(deck.cut())]

while players[0].hand.cards != [] and players[1].hand.cards != []:
    for player in players:
        print(player)

    input("Enter to play: ")

    card1 = players[0].hand.remove()
    card2 = players[1].hand.remove()

    if card1[0] > card2[0]:
        print("{name} wins!".format(name = players[0].name))
        players[0].hand.add(card2)
        players[0].hand.add(card1)
    elif card2[0] > card1[0]:
        print("{name} wins!".format(name = players[1].name))
        players[1].hand.add(card1)
        players[1].hand.add(card2)
    else:
        print("WAR!")
        stacks = [[card1], [card2]]
        for i in [0, 1]:
            for j in range(3):
                stacks[i].append(players[i].hand.remove())

        card1 = players[0].hand.remove()
        card2 = players[1].hand.remove()

        while card1[0] == card2[0]:
            print("MORE WAR!")
            stacks[0].append(card1)
            stacks[0].append(players[0].hand.remove())
            stacks[1].append(card2)
            stacks[1].append(players[1].hand.remove())

            card1 = players[0].hand.remove()
            card2 = players[1].hand.remove()

        if card1[0] > card2[0]:
            print("{name} wins!".format(name = players[0].name))
            for card in stacks[1]:
                players[0].hand.add(card)
            players[0].hand.add(card2)
            for card in stacks[0]:
                players[0].hand.add(card)
            players[0].hand.add(card1)
        else:
            print("{name} wins!".format(name = players[1].name))
            for card in stacks[0]:
                players[1].hand.add(card)
            players[1].hand.add(card1)
            for card in stacks[1]:
                players[1].hand.add(card)
            players[1].hand.add(card2)
