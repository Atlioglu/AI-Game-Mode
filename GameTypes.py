import time

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
            time.sleep(0.4)

    

    def play_game2(self):
            # Ask the user to select the bot level
            print("Select the level of your opponent bot: ")
            print("For Beginner '1', Semi-pro '2', Professional '3', World class '4'")
            level = input("Enter the level (1-4): ").strip()

            # Define the behavior based on the level
            if level == '1':
                bot_strategy = self.algorithms.select_corner_or_edge  # Beginner bot
            elif level == '2':
                bot_strategy = self.algorithms.select_greedy  # Semi-pro bot
            elif level == '3':
                bot_strategy = self.algorithms.select_the_prevented  # Professional bot
            elif level == '4':
                bot_strategy = self.algorithms.select_the_best_move_with_edges  # World-class bot
            else:
                print("Invalid input. Defaulting to Beginner bot.")
                bot_strategy = self.algorithms.select_corner_or_edge

            # Start the game loop
            while True:
                black_moves = self.actions.set_the_available_move('black',self.actions.board)
                white_moves = self.actions.set_the_available_move('white',self.actions.board)
                
                if not black_moves and not white_moves:
                    print("No available moves for both players. Game over!")
                    self.actions.count_pieces()  
                    break

                if black_moves:
                    new_cell_black = self.algorithms.play_each_other('black')
                    self.actions.flip_the_cell('black', new_cell_black,0)
                    self.view.print_board()
                else:
                    print("No available moves for black. Turn skipped.")
                

                white_moves = self.actions.set_the_available_move('white',self.actions.board)

                if white_moves:
                    new_cell_white = bot_strategy('white')
                    self.actions.flip_the_cell('white', new_cell_white,0)
                    self.view.print_board()
                else:
                    print("No available moves for white. Turn skipped.")
                if not black_moves and not white_moves:
                    print("No available moves for both players. Game over!")
                    self.actions.count_pieces()
                    break


                # Check for end of game
                black_moves = self.actions.set_the_available_move('black',self.actions.board)
                white_moves = self.actions.set_the_available_move('white',self.actions.board)
                if not black_moves and not white_moves:
                    print("No available moves for both players. Game over!")
                    self.actions.count_pieces()
                    break
                time.sleep(0.4)



    def play_game3(self):
            #select the bot level
            print("Select the level of the first bot: ")
            print("For Beginner '1', Semi-pro '2', Professional '3', World class '4'")
            level1 = input("Enter the level (1-4): ").strip()
            
            
            # Define the behavior based on the level
            if level1 == '1':
                bot_strategy1 = self.algorithms.select_corner_or_edge  # Beginner bot
            elif level1 == '2':
                bot_strategy1 = self.algorithms.select_greedy  # Semi-pro bot
            elif level1 == '3':
                bot_strategy1 = self.algorithms.select_the_prevented  # Professional bot
            elif level1 == '4':
                bot_strategy1 = self.algorithms.select_the_best_move_with_edges  # World-class bot
            else:
                print("Invalid input. Defaulting to Beginner bot.")
                bot_strategy1 = self.algorithms.select_corner_or_edge

            print("Select the level of the second bot: ")
            print("For Beginner '1', Semi-pro '2', Professional '3', World class '4'")
            level2 = input("Enter the level (1-4): ").strip()

            # Define the behavior based on the level
            if level2 == '1':
                bot_strategy2 = self.algorithms.select_corner_or_edge  # Beginner bot
            elif level2 == '2':
                bot_strategy2 = self.algorithms.select_greedy  # Semi-pro bot
            elif level2 == '3':
                bot_strategy2 = self.algorithms.select_the_prevented  # Professional bot
            elif level2 == '4':
                bot_strategy2 = self.algorithms.select_the_best_move_with_edges  # World-class bot
            else:
                print("Invalid input. Defaulting to Beginner bot.")
                bot_strategy2 = self.algorithms.select_corner_or_edge

            # Start the game
            while True:
                black_moves = self.actions.set_the_available_move('black',self.actions.board)
                white_moves = self.actions.set_the_available_move('white',self.actions.board)

                if not black_moves and not white_moves:
                    print("No available moves for both players. Game over!")
                    self.actions.count_pieces()  
                    break

                if black_moves:
                    new_cell_black = bot_strategy1('black')
                    self.actions.flip_the_cell('black', new_cell_black,0)
                    self.view.print_board()

                else:
                    print("No available moves for black. Turn skipped.")
                
                white_moves = self.actions.set_the_available_move('white',self.actions.board)

                if white_moves:
                    new_cell_white = bot_strategy2('white')
                    self.actions.flip_the_cell('white', new_cell_white,0)
                    self.view.print_board()
                else:
                    print("No available moves for white. Turn skipped.")
                if not black_moves and not white_moves:
                    print("No available moves for both players. Game over!")
                    self.actions.count_pieces()
                    break
                time.sleep(0.2)
