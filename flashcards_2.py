class FlashCard:
    """FlashCard class docstring"""

    def __init__(self, card_term='', card_definition=''):
        self.term = card_term
        self.definition = card_definition

    def __str__(self):
        return f'Card:\n{self.term}\nDefinition:\n{self.definition}'


if __name__ == '__main__':
    term, definition, ans = [input() for i in range(3)]
    card = FlashCard(term, definition)
    print('right' if ans == card.definition else 'wrong')
