import argparse
import io
import random

# CL arguments
parser = argparse.ArgumentParser(description='Stage 7/7: IMPORTant')
parser.add_argument('--import_from', type=str, help="File name to import FlashCards from")
parser.add_argument('--export_to', type=str, help="File name to export FlashCards to")
args = parser.parse_args()

# StringIO handler
stream = io.StringIO()


def input_and_log() -> str:
    user_input = input()
    print(user_input, file=stream)
    return user_input


def print_and_log(msg: str):
    print(msg)
    print(msg, file=stream)


class FlashCard:
    def __init__(self, term: str, definition: str, mistakes: int = 0):
        self.term = term
        self.definition = definition
        self.mistakes = mistakes


class FlashCardGame:
    """FlashCardGame class docstring"""

    def __init__(self):
        self.Deck = []
        if args.import_from is not None:
            self.import_cards(args.import_from)

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
                    print_and_log('Bye bye!')
                    if args.export_to is not None:
                        self.export_cards(args.export_to)
                    break
                case 'log':
                    self.log()
                case 'hardest card':
                    self.hardest()
                case 'reset stats':
                    self.reset()

    def terms(self):
        return [card.term for card in self.Deck]

    def definitions(self):
        return [card.definition for card in self.Deck]

    def mistakes(self):
        return [card.mistakes for card in self.Deck]

    def index_of_term(self, term) -> int:
        return self.terms().index(term)

    def index_of_definition(self, definition) -> int:
        return self.definitions().index(definition)

    def add_card(self):
        # Loop to get a valid term
        print_and_log('The card:')
        term = input_and_log()
        while term in self.terms():
            print_and_log(f'The card "{term}" already exists. Try again:')
            term = input_and_log()
        # Loop to get a valid definition
        print_and_log('The definition of the card:')
        definition = input_and_log()
        while definition in self.definitions():
            print_and_log(f'The definition "{definition}" already exists. Try again:')
            definition = input_and_log()
        # Add card to collection
        self.Deck.append(FlashCard(term, definition))
        print_and_log(f'The pair ("{term}":"{definition}") has been added.')

    def remove_card(self):
        print_and_log('Which card?')
        term = input()
        if term in self.terms():
            del self.Deck[self.index_of_term(term)]
            print_and_log('The card has been removed.')
        else:
            print_and_log(f'Can\'t remove "{term}": there is no such card.')

    def import_cards(self, file_name: str = ''):
        if not file_name:
            print_and_log('File name:')
            file_name = input_and_log()
        try:
            with open(file_name, 'r') as f:
                cards_to_import = [line.strip() for line in f.readlines()]
                for card in cards_to_import:
                    term, definition, mistakes = card.split()
                    if term in self.terms():
                        self.Deck[self.index_of_term(term)] = FlashCard(term, definition, int(mistakes))
                    else:
                        self.Deck.append(FlashCard(term, definition, int(mistakes)))
                print_and_log(f'{len(cards_to_import)} cards have been loaded.')
        except FileNotFoundError:
            print_and_log('File not found.')

    def export_cards(self, file_name: str = ''):
        if not file_name:
            print_and_log('File name:')
            file_name = input_and_log()
        # TODO open file error handling
        with open(file_name, 'w') as f:
            cards_to_export = [f'{card.term} {card.definition} {card.mistakes}' for card in self.Deck]
            f.write('\n'.join(cards_to_export))
            print_and_log(f'{len(cards_to_export)} cards have been saved.')

    def ask(self):
        print_and_log('How many times to ask?')
        # TODO Input validation
        for _ in range(int(input_and_log())):
            card = random.choice(self.Deck)
            print_and_log(f'Print the definition of "{card.term}":')
            ans = input_and_log()
            if ans == card.definition:
                print_and_log('Correct!')
            elif ans in self.definitions():
                card.mistakes += 1
                correct_term = self.Deck[self.index_of_definition(ans)].term
                print_and_log(f'Wrong. The right answer is "{card.definition}", '
                              f'but your definition is correct for "{correct_term}".')
            else:
                card.mistakes += 1
                print_and_log(f'Wrong. The right answer is "{card.definition}".')

    @staticmethod
    def get_action() -> str:
        while True:
            try:
                print_and_log(
                    'Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')
                user_input = input_and_log()
                if user_input in ['add', 'remove', 'import', 'export', 'ask', 'exit', 'log', 'hardest card',
                                  'reset stats']:
                    return user_input
                else:
                    raise ValueError
            except ValueError:
                print_and_log("Wrong action. Please type one of the available options:")

    @staticmethod
    def log():
        print_and_log('File name:')
        with open(input_and_log(), 'w') as f:
            f.write(stream.getvalue())
        print_and_log('The log has been saved.')

    def hardest(self):
        max_mistakes = max(self.mistakes()) if len(self.mistakes()) != 0 else 0
        num_of_cards = self.mistakes().count(max_mistakes)
        if max_mistakes == 0:
            print_and_log('There are no cards with errors.')
        elif num_of_cards == 1:
            index = self.mistakes().index(max_mistakes)
            print_and_log(f'The hardest card is "{self.Deck[index].term}". '
                          f'You have {max_mistakes} errors answering it.')
        else:
            terms = ', '.join(f'"{card.term}"' for card in self.Deck if card.mistakes == max_mistakes)
            print_and_log(f'The hardest cards are {terms}.')

    def reset(self):
        for card in self.Deck:
            card.mistakes = 0
        print_and_log('Card statistics have been reset.')


if __name__ == '__main__':
    game = FlashCardGame()
    game.play()
