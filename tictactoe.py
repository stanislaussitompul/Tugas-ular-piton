class TicTacToe:
    def _init_(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def display_board(self):
        print("-------------")
        for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
            print("|", *row, "|")
            print("-------------")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return self.board[combination[0]]
        if ' ' not in self.board:
            return 'Tie'
        return None

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        while True:
            self.display_board()
            position = int(input("Enter a position (1-9): ")) - 1

            if position in range(9) and self.make_move(position):
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    if winner == 'Tie':
                        print("It's a tie!")
                    else:
                        print("Player", winner, "wins!")
                    break

                self.switch_player()
            else:
                print("Invalid move. Try again.")


# Start the game
game = TicTacToe()
game.play_game()
