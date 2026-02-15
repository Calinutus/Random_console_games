from Tic_Tac_Toe.Repo import BoardRepository
from Tic_Tac_Toe.Logic import GameEngine
from Tic_Tac_Toe.UI import ConsoleUI

def main():
    print("X / 0")
    ui = ConsoleUI()

    while True:
        human = input("Choose X or O: ").upper()
        if human in ("X", "O"):
            break
        print("X OR O")

    repo = BoardRepository()
    game = GameEngine(repo, human)



    print("\n Placement Phase")

    while game.human_pieces < 4 or game.computer_pieces < 4:
        ui.show_board(game.board)

        if game.turn == game.human and game.human_pieces < 4:
            print("Player turn")
            r, c = ui.get_placement_input(game.board)
            game.board.place(r, c, game.human)
            game.human_pieces += 1


            if game.board.check_win(game.human):
                ui.show_board(game.board)
                print("Player win during placement")
                return

        elif game.turn == game.computer_player and game.computer_pieces < 4:
            game.computer_place()
            game.computer_pieces += 1

            if game.board.check_win(game.computer_player):
                ui.show_board(game.board)
                print("Computer win durin placement")
                return

        game.switch_turn()

    print("\n Movement")

    while True:
        ui.show_board(game.board)

        if game.turn == game.human:
            print("Player move")
            (r1, c1), (r2, c2) = ui.get_move_input(game.board, game.human)
            game.board.move(r1, c1, r2, c2)

            if game.board.check_win(game.human):
                ui.show_board(game.board)
                print("You w")
                return

        else:
            print("Computer moving")
            game.computer_move()

            if game.board.check_win(game.computer_player):
                ui.show_board(game.board)
                print("Computer win")
                return

        game.switch_turn()


if __name__ == "__main__":
    main()
