import random
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Game:
    # Initialize the 3x3 board with empty spaces
    def __init__(self, size=3, mode="AI"):
        self.current_player = None
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.mode = mode
        self.win_condition = size  # Adjust the win condition for larger boards
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("AI" if mode == "AI" else "Player 2", "O")
        self.current_player = self.player1
        self.scores = {"Player 1": 0, "Player 2": 0, "AI": 0, "Draw": 0}
        self.history = []

    def display_board(self):
        # Print the current board state
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, player):
        # Ask the player to make a move
        if player.name == "AI":
            self.ai_move()
        else:
            while True:
                try:
                    row = int(input(f"{player.name}, enter the row (0, 1, 2): "))
                    col = int(input(f"{player.name}, enter the column (0, 1, 2): "))
                    if self.board[row][col] == " ":
                        self.board[row][col] = player.symbol
                        self.history.append((row, col))
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
    
    def ai_move(self):
        empty_cells = [(r, c) for r in range(self.size) for c in range(self.size) if self.board[r][c] == " "]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = self.player2.symbol  # AI uses the symbol 'O'
            self.history.append((row, col))

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
                self.update_score(self.current_player)
                break
            elif self.check_draw():
                self.display_board()
                print("It's a draw!")
                self.update_score("Draw")
                break

            self.switch_player(player1, player2)

        if input("Play again? (y/n): ").lower() == "y":
            self.__init__()  # Reset the game
            self.play()
    
    def update_score(self, winner):
        if winner == "Draw":
            self.scores["Draw"] += 1
        else:
            self.scores[winner(self.name)] += 1

    def display_score(self):
        print(f"Scores: {self.scores}")

if __name__ == "__main__":
    game = Game()
    game.play()
