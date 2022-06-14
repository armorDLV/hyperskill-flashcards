import random


class FlashCardGame:
    """FlashCardGame class docstring"""

    def __init__(self):
        self.terms = []
        self.definitions = []

    def play(self):
        while True:
            match self.get_action():
                case 'add':
                    self.add_card()
                case 'remove':
                    self.remove_card()
                case 'import':
                    self.import_cards()
                case 'export':
                    self.export_cards()
                case 'ask':
                    self.ask()
                case 'exit':
                    print('Bye bye!')
                    break

    def add_card(self):
        # Loop to get a valid term
        print('The card:')
        term = input()
        while term in self.terms:
            print(f'The card "{term}" already exists. Try again:')
            term = input()
        pass
        # Loop to get a valid definition
        print('The definition of the card:')
        definition = input()
        while definition in self.definitions:
            print(f'The definition "{definition}" already exists. Try again:')
            definition = input()
        # Add card to collection
        self.terms.append(term)
        self.definitions.append(definition)
        print(f'The pair ("{term}":"{definition}") has been added.')

    def remove_card(self):
        print('Which card?')
        term = input()
        if term in self.terms:
            index = self.terms.index(term)
            del self.terms[index]
            del self.definitions[index]
            print('The card has been removed.')
        else:
            print(f'Can\'t remove "{term}": there is no such card.')

    def import_cards(self):
        print('File name:')
        try:
            with open(input(), 'r') as f:
                cards_to_import = [line.strip() for line in f.readlines()]
                for card in cards_to_import:
                    term, definition = card.split()
                    if term in self.terms:
                        index = self.terms.index(term)
                        self.terms[index] = term
                        self.definitions[index] = definition
                    else:
                        self.terms.append(term)
                        self.definitions.append(definition)
                print(f'{len(cards_to_import)} cards have been loaded.')
        except FileNotFoundError:
            print('File not found.')

    def export_cards(self):
        print('File name:')
        # TODO File error handling
        with open(input(), 'w') as f:
            cards_to_export = [f'{term} {definition}' for term, definition in zip(self.terms, self.definitions)]
            f.write('\n'.join(cards_to_export))
            print(f'{len(cards_to_export)} cards have been saved.')

    def ask(self):
        print('How many times to ask?')
        # TODO Input validation
        for _ in range(int(input())):
            term = random.choice(self.terms)
            definition = self.definitions[self.terms.index(term)]
            print(f'Print the definition of "{term}":')
            ans = input()
            if ans == definition:
                print('Correct!')
            elif ans in self.definitions:
                correct_term = self.terms[self.definitions.index(ans)]
                print(f'Wrong. The right answer is "{definition}",',
                      f'but your definition is correct for "{correct_term}".')
            else:
                print(f'Wrong. The right answer is "{definition}".')

    @staticmethod
    def get_action() -> str:
        while True:
            try:
                print('Input the action (add, remove, import, export, ask, exit):')
                user_input = input()
                if user_input in ['add', 'remove', 'import', 'export', 'ask', 'exit']:
                    return user_input
                else:
                    raise ValueError
            except ValueError:
                print("Wrong action. Please type one of the available options:")


if __name__ == '__main__':
    game = FlashCardGame()
    game.play()
