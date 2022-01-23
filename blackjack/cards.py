from random import shuffle


suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


class Card:
    def __init__(self, rank:str, suit:str, value:int) -> None:
        self.rank = rank
        self.suit = suit
        self.value = value
    
    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self, n:int=1) -> None:      
        self.cartas = []

        for suit in suits:
            for i in range(len(ranks)):
                self.cartas.append(Card(ranks[i], suit, values[i]))
        
        self.cartas = self.cartas * n

        shuffle(self.cartas)

        self.cartas_descartadas = []

    def pick_card(self):
        carta = self.cartas.pop()
        self.cartas_descartadas.append(carta)

        return carta


if __name__ == '__main__':
    d = Deck()
    print(d.pick_card())
    print(len(d.cartas))