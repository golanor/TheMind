from abc import ABC, abstractmethod

import numpy as np


class Player(ABC):
    def __init__(self, cards: np.array):
        self.cards = cards

    @abstractmethod
    def play(self, cards_remaining: list[int], top_card: int):
        pass


class Deck:
    def __init__(self, n_cards: int = 100):
        self.cards = np.arange(1, n_cards+1)
        np.random.shuffle(self.cards)

    def draw(self, level: int, n_players: int = 2):
        n_cards = n_players * level
        cards = self.cards[:n_cards]
        for p in range(n_players):
            yield sorted(cards[p*level:(p+1)*level])

class Game:
    def __init__(self, n_players: int, *, n_cards: int = 100):
        self.n_players = n_players
        self.deck = Deck(n_cards)
        self.round = 0
        self.mistakes = 0

    def _round(self, level: int):
