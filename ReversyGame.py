import random
from GameView import GameView
from GameActions import GameActions
from Algorithms import Algorithms
from GameTypes import GameTypes
from GamePlayTree import GamePlayTree
from GamePlayTree import GamePlayTree


class ReversyGame:
    def __init__(self):
        self.board = [['' for _ in range(8)] for _ in range(8)]
        self.board[4][3] = 'black'
        self.board[3][4] = 'black'
        self.board[3][3] = 'white'
        self.board[4][4] = 'white'
        self.view = GameView(self.board)
        self.actions = GameActions(self.board)
        self.algorithms = Algorithms(self.actions)
        self.game_types = GameTypes(self.actions, self.algorithms, self.view)
        self.game_tree = GamePlayTree(board=self.board)  

    

    def start_game(self):
        print("Welcome to the 4x4 Game!")
        print("Choose the type of game:")
        print("1: Play with another player")
        print("2: Play against the bot")
        print("3: Watch the bots play")

        while True:
            game_type = input("Enter your choice (1, 2, or 3): ").strip()
            if game_type == '1':
                print("Starting a 2-player game!")
                return game_type
            elif game_type == '2':
                print("The game is starting against the bot!")
                return game_type
            elif game_type == '3':
                print("Bot vs Bot mode is starting now.")
                return game_type
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
    

if __name__ == "__main__":
    game = ReversyGame()
    game_type = game.start_game()
    game.actions.print_board()
    if game_type == '1':
        game.game_types.play_game1()
    elif game_type == '2':
        game.game_types.play_game2()
    elif game_type == '3':
        game.game_types.play_game3()
    else:
        print("error")

