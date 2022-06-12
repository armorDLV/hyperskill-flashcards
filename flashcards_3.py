class FlashCard:
    """FlashCard class docstring"""

    def __init__(self, card_term='', card_definition=''):
        self.term = card_term
        self.definition = card_definition

    def __str__(self):
        return f'Card:\n{self.term}\nDefinition:\n{self.definition}'

    def test(self):
        print(f'Print the definition of "{self.term}":')
        ans = input()
        print('Correct!' if ans == self.definition else f'Wrong. The right answer is "{self.definition}".')


class FlashCardGame:
    """FlashCardGame class docstring"""

    def __init__(self):
        self.cards = []
        print('Input the number of cards:')
        self.num_of_cards = int(input())
        for i in range(1, self.num_of_cards + 1):
            print(f'The term for card #{i}:')
            term = input()
            print(f'The definition for card #{i}: ')
            definition = input()
            self.cards.append(FlashCard(term, definition))

    def play(self):
        for card in self.cards:
            card.test()


if __name__ == '__main__':
    game = FlashCardGame()
    game.play()
