from random import shuffle
from functools import wraps
import csv

def log(fn):
    @wraps(fn)
    def wrapper(*args):
        with open("deck.log", "w") as file:
            file.write("{} has arguments: {}".format(fn.__name__, *args))
        #print("{} has arguments{}".format(fn.__name__, *args))
        return fn(*args)
    return wrapper

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return "{} {}".format(self.suit, self.value)

class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.cards = []
        self.count = 0
        #self.reset()


    def save_deck(self):
        with open("deck.csv", "w") as csvfile:
            data_writer = csv.writer(csvfile, delimiter=",")
            for card in self.cards:
                data_writer.writerow([card])

    def load_deck(self):
        with open("deck.csv", "r") as csvfile:
            reader = csv.reader(csvfile, delimiter = ",")
            rows = list(reader)
            for row in rows:
                self.cards.append(row)

    def __str__(self):
        return "Cards in the deck: {}".format(len(self.cards))

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count < 52:
            next_value = self.cards[self.count]
            return next_value
        elif self.count >= 52:
            raise StopIteration

    def deal(self):
        """Remove one card from the back"""
        if len(self.cards) < 1:
            return False
        else:
            return self.cards.pop()

    @log
    def shuffle(self):
        """Shuffle the order of the cards deck"""
        if len(self.cards) < 52:
            return False
        else:
            shuffle(self.cards)
            return self

    def reset(self):
        """Reset the cards deck"""
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit, value))


deck = Deck()


# for card in deck
#     print(card)
