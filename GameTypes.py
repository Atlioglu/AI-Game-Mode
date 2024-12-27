class GameTypes:
    def __init__(self, actions, algorithms, view):
        self.actions = actions
        self.algorithms = algorithms
        self.view = view

    def play_game1(self):
        while True:
            new_cell = self.algorithms.play_each_other('black')
            self.actions.flip_the_cell('black', new_cell)
            self.view.print_board()
            new_cell_white = self.algorithms.play_each_other('white')
            self.actions.flip_the_cell('white', new_cell_white)
            self.view.print_board()
    
    def play_game2(self):
        while True:
            # Black player
            new_cell = self.algorithms.play_each_other('black')
            if new_cell is None:
                print("No valid moves for black. Turn skipped.")
            else:   
                self.actions.flip_the_cell('black', new_cell)
                self.view.print_board()

            # White player
            new_cell_white = self.algorithms.select_random('white')
            if new_cell_white is None:
                print("No valid moves for white. Turn skipped.")
            else:
                self.actions.flip_the_cell('white', new_cell_white)
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
                new_cell = self.algorithms.select_random('black')
                self.actions.flip_the_cell('black', new_cell)
                self.view.print_board()

            else:
                print("No available moves for black. Turn skipped.")

            if white_moves:
                new_cell_white = self.algorithms.select_random('white')
                self.actions.flip_the_cell('white', new_cell_white)
                self.view.print_board()
            else:
                print("No available moves for white. Turn skipped.")
    