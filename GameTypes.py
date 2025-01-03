class GameTypes:
    def __init__(self, actions, algorithms, view):
        self.actions = actions
        self.algorithms = algorithms
        self.view = view

    def play_game1(self):
        while True:
            new_cell_black = self.algorithms.play_each_other('black')
            self.actions.flip_the_cell('black', new_cell_black,0)
            self.view.print_board()
            new_cell_white = self.algorithms.play_each_other('white')
            self.actions.flip_the_cell('white', new_cell_white,0)
            self.view.print_board()
    
    def play_game2(self):
        while True:
            new_cell_black = self.algorithms.play_each_other('black')
            if new_cell_black is None:
                print("No valid moves for black. Turn skipped.")
            else:   
                self.actions.flip_the_cell('black', new_cell_black,0)
                self.view.print_board()

            new_cell_white = self.algorithms.select_random('white')
            if new_cell_white is None:
                print("No valid moves for white. Turn skipped.")
            else:
                self.actions.flip_the_cell('white', new_cell_white,0)
                self.view.print_board()

            # Check for end of game
            black_moves = self.actions.set_the_available_move('black')
            white_moves = self.actions.set_the_available_move('white')
            if not black_moves and not white_moves:
                print("No available moves for both players. Game over!")
                self.actions.count_pieces()
                break
        
    def play_game3(self):
        while True:
            black_moves = self.actions.set_the_available_move('black')
            white_moves = self.actions.set_the_available_move('white')
            
            if not black_moves and not white_moves:
                print("No available moves for both players. Game over!")
                self.actions.count_pieces()  
                break

            if black_moves:
                new_cell_black = self.algorithms.select_random('black')
                self.actions.flip_the_cell('black', new_cell_black,0)
                self.view.print_board()

            else:
                print("No available moves for black. Turn skipped.")

            if white_moves:
                new_cell_white = self.algorithms.select_random('white')
                self.actions.flip_the_cell('white', new_cell_white,0)
                self.view.print_board()
            else:
                print("No available moves for white. Turn skipped.")



    def play_game2new(self):
            # Ask the user to select the bot level
            print("Select the level of your opponent bot: ")
            print("For Beginner '1', Semi-pro '2', Professional '3', World class '4'")
            level = input("Enter the level (1-4): ").strip()

            # Define the behavior based on the level
            if level == '1':
                bot_strategy = self.algorithms.select_random  # Beginner bot
            elif level == '2':
                bot_strategy = self.algorithms.select_the_best_next  # Semi-pro bot
            elif level == '3':
                bot_strategy = self.algorithms.select_the_prevented  # Professional bot
            elif level == '4':
                bot_strategy = self.algorithms.select_the_best_next  # World-class bot
            else:
                print("Invalid input. Defaulting to Beginner bot.")
                bot_strategy = self.algorithms.select_random

            # Start the game loop
            while True:
                # Black player
                new_cell_black = self.algorithms.play_each_other('black')
                if new_cell_black is None:
                    print("No valid moves for black. Turn skipped.")
                else:
                    self.actions.flip_the_cell('black', new_cell_black,0)
                    self.view.print_board()

                # White player (bot)
                new_cell_white = bot_strategy('white')
                if new_cell_white is None:
                    print("No valid moves for white. Turn skipped.")
                else:
                    self.actions.flip_the_cell('white', new_cell_white,0)
                    self.view.print_board()

                # Check for end of game
                black_moves = self.actions.set_the_available_move('black')
                white_moves = self.actions.set_the_available_move('white')
                if not black_moves and not white_moves:
                    print("No available moves for both players. Game over!")
                    self.actions.count_pieces()
                    break

    