from random import shuffle

suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# List comprehension
mycards = [(s,r) for s in suite for r in ranks]

class Deck():

    def __init__(self):
        print('Creating New Deck')
        self.allcards = mycards

    def shuffle(self):
        print("Shuffling the Deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])


class Hand():
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:

    def __init__(self):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.

