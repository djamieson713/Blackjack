class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        result = self.rank + ' of ' + self.suit
        return result
