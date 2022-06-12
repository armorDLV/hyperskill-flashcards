class FlashCardGame:
    """FlashCardGame class docstring"""

    def __init__(self):
        self.cards_dict = {}
        print('Input the number of cards:')
        for _ in range(int(input())):
            self.add_card()

    def add_card(self):
        print(f'The term for card #{len(self.cards_dict) + 1}:')
        term = input()
        while term in self.cards_dict.keys():
            print(f'The term "{term}" already exists. Try again:')
            term = input()

        print(f'The definition for card #{len(self.cards_dict) + 1}: ')
        definition = input()
        while definition in self.cards_dict.values():
            print(f'The definition "{definition}" already exists. Try again:')
            definition = input()

        self.cards_dict[term] = definition

    def play(self):
        for term, definition in self.cards_dict.items():
            print(f'Print the definition of "{term}":')
            ans = input()
            if ans == definition:
                print('Correct!')
            elif ans in self.cards_dict.values():
                correct_term = list(self.cards_dict.keys())[list(self.cards_dict.values()).index(ans)]
                print(f'Wrong. The right answer is "{definition}",',
                      f'but your definition is correct for "{correct_term}".')
            else:
                print(f'Wrong. The right answer is "{definition}".')


if __name__ == '__main__':
    game = FlashCardGame()
    game.play()
