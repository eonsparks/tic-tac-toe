class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Game:
    def __init__(self):
        # Initialize the 3x3 board with empty spaces
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = None

    def display_board(self):
        # Print the current board state
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, player):
        # Ask the player to make a move
        while True:
            try:
                row = int(input(f"{player.name}, enter the row (0, 1, 2): "))
                col = int(input(f"{player.name}, enter the column (0, 1, 2): "))
                if self.board[row][col] == " ":
                    self.board[row][col] = player.symbol
                    break
                else:
                    print("That spot is already taken, Try again!")
            except (ValueError, IndexError):
                print("Invalid input! Please enter numbers between 0 and 2!")

    def check_winner(self, player):
        # Check rows, columns, and diagonals for a win
        symbol = player.symbol
        for row in self.board:
            if all([cell == symbol for cell in row]):
                return True

        for col in range(3):
            if all([self.board[row][col] == symbol for row in range(3)]):
                return True

        if all([self.board[i][i] == symbol for i in range(3)]) or \
           all([self.board[i][2 - i] == symbol for i in range(3)]):
            return True

        return False

    def check_draw(self):
        # Check if the board is full and there is no winner
        return all([cell != " " for row in self.board for cell in row])

    def switch_player(self, player1, player2):
        # Switch the current player
        self.current_player = player2 if self.current_player == player1 else player1

    def play(self):
        # Main game loop
        print("Welcome to Tic-Tac-Toe!")
        player1 = Player(input("Enter Player 1's name: "), "X")
        player2 = Player(input("Enter Player 2's name: "), "O")
        self.current_player = player1

        while True:
            self.display_board()
            self.make_move(self.current_player)

            if self.check_winner(self.current_player):
                self.display_board()
                print(f"Congratulations {self.current_player.name}, you win!")
                break
            elif self.check_draw():
                self.display_board()
                print("It's a draw!")
                break

            self.switch_player(player1, player2)

        if input("Play again? (y/n): ").lower() == "y":
            self.__init__()  # Reset the game
            self.play()

if __name__ == "__main__":
    game = Game()
    game.play()
