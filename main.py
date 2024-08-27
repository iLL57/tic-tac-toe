import game

game = game.TicTacToe()

while True:
    game.display_board()

    while True:
        row, col = game.get_player_choice()
        game.update_board(row, col)
        game.display_board()

        if game.check_win():
            print(f"Player {game.current_player} wins!")
            break
        if game.check_draw():
            print("It's a draw")
            break

        game.switch_player()

    if not game.play_again():
        print("Thanks for playing!")
        break
