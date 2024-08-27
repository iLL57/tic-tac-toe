import os
import sys
import colorama
from colorama import Fore, Style


class TicTacToe:
    def __init__(self):
        colorama.init(autoreset=True)
        self.board = None
        self.reset_board()
        self.current_player = 'X'
        # Initialize the board as a 3x3 matrix with numbers 1-9 for easy reference

    def reset_board(self):
        self.board = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]

    def clear_screen(self):
        # Check if the terminal environment variable is set
        if os.getenv('TERM') or os.name == 'nt':  # Windows usually handles this differently
            # Clear the console screen in a platform-independent way
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            # Fallback: Print several newlines to simulate clearing the screen
            print("\n" * 50)

    def display_board(self):
        self.clear_screen()
        for row in self.board:
            colored_row = [self.get_colored_cell(cell) for cell in row]
            print('|'.join(colored_row))
            print('-' * 5)

    def get_colored_cell(self, cell):
        # Return the cell with appropriate color based on its value
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.GREEN + cell + Style.RESET_ALL
        else:
            return cell

    def get_player_choice(self):
        while True:
            move_str = input(f"Where would you like to go {self.current_player}? Choose 1-9.\n")

            # Checks for multiple characters
            if len(move_str) > 1:
                print("Invalid input. Please enter a single digit 1-9.")
                continue

            # Checks for empty input
            if not move_str:
                print("Oops! Nothing was entered. Please enter a number 1-9.")
                continue

            try:
                move = int(move_str)
                if move < 1 or move > 9:
                    print("Invalid selection. Please try again")
                    continue
                row, col = divmod(move - 1, 3)
                if self.board[row][col] in ['X', 'O']:
                    print('Space is already taken. Choose again.')
                else:
                    return row, col
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

    def update_board(self, row, col):
        # Update the board with the current player's symbol
        self.board[row][col] = self.current_player

    def switch_player(self):
        # Switch the current player to the other player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        for i in range(3):
            # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            # Check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
            # Check diagonals
            if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return True
            if self.board[0][2] == self.board[1][1] == self.board[2][0]:
                return True
            return False

    def check_draw(self):
        for row in self.board:
            if any(cell not in ['X', 'O'] for cell in row):
                return False
        return True

    def play_again(self):
        while True:
            restart = input("Would you like to play again? (y/n): ").lower()
            if restart == 'y':
                self.reset_board()
                if self.current_player == 'X':
                    self.current_player = 'O'
                    return True
                else:
                    self.current_player = 'X'
                    return True
            elif restart == 'n':
                return False
            else:
                print("Invalid input. Please enter 'y' to restart or 'n' to exit game.")
