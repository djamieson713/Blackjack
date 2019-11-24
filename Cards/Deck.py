import random
import Cards

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = Cards.Card(suit, rank)
                self.deck.append(card)

    def __str__(self):
        result = ''
        for card in self.deck:
            result = result + card.__str__() + ','
        return result

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, numcards):
        result = []
        for i in range(0, numcards):
            result.append(self.deck.pop())
        return result
