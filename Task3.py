class Cell():
    def __init__(self, number):
        self.number = number
        self.symbol = " "
        self.occupied = False


class Board():
    def __init__(self):
        self.current_state = []
        for i in range(1, 10):
            self.current_state.append(Cell(i))

    def change_cell(self, cell_number, symbol):
        cell = self.current_state[cell_number - 1]
        if cell.occupied:
            return False
        cell.symbol = symbol
        cell.occupied = True
        return True

    def display_board(self):
        print('-------------')
        for i in range(0, 9, 3):
            print(
                f"|{self.current_state[i].symbol}|{self.current_state[i + 1].symbol}|{self.current_state[i + 2].symbol}|")
        print('-------------')

    def is_end(self):
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтальные линии
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)  # диагонали
        ]
        for pos in win_positions:
            if self.current_state[pos[0]].symbol != " " and self.current_state[pos[0]].symbol == self.current_state[
                pos[1]].symbol == self.current_state[pos[2]].symbol:
                return True
        return False

    def reset_board(self):
        for cell in self.current_state:
            cell.symbol = " "
            cell.occupied = False


class Player():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0

    def make_move(self):
        while True:
            try:
                move = int(input(f'{self.name}, enter the number of cell for your turn(1-9): '))
                if move < 1 or move > 9:
                    raise ValueError
                return move
            except ValueError:
                print("Input error. Please, enter the number between 1 and 9.")


class Game():
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.board = Board()

    def one_turn(self, player):
        while True:
            self.board.display_board()
            cell_number = player.make_move()
            if self.board.change_cell(cell_number, player.symbol):
                if self.board.is_end():
                    return True
                return False
            print('Cell is occupied. Make another move.')

    def play_one_game(self):
        print('Game has started!')
        while True:
            for player in self.players:
                if self.one_turn(player):
                    self.board.display_board()
                    print(f'Congratulations, {player.name}! You won!')
                    player.wins += 1
                    return
                if all(cell.occupied for cell in self.board.current_state):
                    self.board.display_board()
                    print('Draw in the game')
                    return

    def start_games(self):
        print("Welcome to Tic Tac Toe game!")
        while True:
            self.board.reset_board()
            self.play_one_game()
            print(
                f"Count: {self.players[0].name} - {self.players[0].wins}, {self.players[1].name} - {self.players[1].wins}")
            again = input("Do you want to continue? (yes/no): ")
            if again.lower() != 'yes':
                print("Thanks for playing!")
                break


if __name__ == '__main__':
    player1 = Player('Harry', 'x')
    player2 = Player('Ron', 'o')
    game = Game(player1, player2)
    game.start_games()
