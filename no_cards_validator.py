class NoCardsValidator():
    def __init__(self, cards):
        self.cards = cards

    def is_valid(self):
        return len(self.cards) == 0

    def valid_cards(self):
        return []