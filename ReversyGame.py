import random


class ReversyGame:
    def __init__(self):
        self.board = [['' for _ in range(8)] for _ in range(8)]
        self.board[4][3] = 'black'
        self.board[3][4] = 'black'
        self.board[3][3] = 'white'
        self.board[4][4] = 'white'
        
    def print_board(self):
        for row in self.board:
            display_row = []
            for cell in row:
                if cell == 'white':
                    display_row.append('W') 
                elif cell == 'black':
                    display_row.append('\033[1;31mO\033[0m') 
                else:
                    display_row.append('_')
            print(' '.join(display_row))

    def is_valid_position(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def set_the_available_move(self, color):
        opponent_color = 'white' if color == 'black' else 'black'
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        available_moves = []

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == color:
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        found_opponent = False

                        while self.is_valid_position(x, y):
                            if self.board[x][y] == '':
                                if found_opponent:
                                    available_moves.append((x, y))
                                break
                            elif self.board[x][y] == opponent_color:
                                found_opponent = True
                            else:
                                break

                            x += dx
                            y += dy
        return list(set(available_moves))
    
    def play_each_other(self, color):
        available_moves = self.set_the_available_move(color)        
        if not available_moves:
            print(f"No available moves for {color}. Turn skipped.")
            return None  

        while True:
            try:
                user_input = input(f"Enter your move for {color} (row, column) or 'q' to quit or 'h' for the hint: ").strip()
                if user_input.lower() == 'q':
                    print("Game ended by the user.")
                    exit()
                elif user_input.lower() == 'h':
                    print(f"Available moves for {color}: {available_moves}")
                    continue

                x_new, y_new = map(int, user_input.split(','))
                new_cell = (x_new, y_new)

                if new_cell not in available_moves:
                    print(f"Error: The cell {new_cell} is not a valid move for {color}. Try again.")
                else:
                    return new_cell 
            except ValueError:
                print("Invalid input. Please enter the row and column as two numbers separated by a comma, or 'q' to quit.")


    def flip_the_cell(self, color,new_cell):
        available_moves = self.set_the_available_move(color)
        x_new, y_new = new_cell      
        if not available_moves:
            print(f"No available moves for {color}. Turn skipped.")
            return

        while True:
            try:
                if new_cell not in available_moves:
                    print(f"Error: The cell {new_cell} is not a valid move for {color}. Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter the row and column as two numbers separated by a comma, or 'q' to quit.")
        

        self.board[x_new][y_new] = color
        opponent_color = 'white' if color == 'black' else 'black'
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        for dx, dy in directions:
            x, y = x_new + dx, y_new + dy
            cells_to_flip = []

            while self.is_valid_position(x, y):
                if self.board[x][y] == opponent_color:
                    cells_to_flip.append((x, y))
                elif self.board[x][y] == color:
                    for cx, cy in cells_to_flip:
                        self.board[cx][cy] = color
                    break
                else:
                    break

                x += dx
                y += dy



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
    

    def select_random(self, color):
        available_moves = self.set_the_available_move(color)
        if not available_moves:
            print(f"No available moves for {color}.")
            return None  

        # Priority 1: Check for corners
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        corner_moves = [move for move in available_moves if move in corners]
        if corner_moves:
            selected_move = random.choice(corner_moves)
            print(f"Corner move selected for {color}: {selected_move}")
            return selected_move

        # Priority 2: Check for edges
        edge_moves = [move for move in available_moves if move[0] in {0, 7} or move[1] in {0, 7}]
        if edge_moves:
            selected_move = random.choice(edge_moves)
            print(f"Edge move selected for {color}: {selected_move}")
            return selected_move

        # Priority 3: Randomly select any move
        random_move = random.choice(available_moves)
        print(f"Randomly selected move for {color}: {random_move}")
        return random_move

    
    def play_game1(self):
        while True:
            new_cell = game.play_each_other('black')
            game.flip_the_cell('black', new_cell)
            game.print_board()
            new_cell_white = game.play_each_other('white')
            game.flip_the_cell('white', new_cell_white)
            game.print_board()
    
    def play_game2(self):
        while True:
            new_cell = game.play_each_other('black')
            if new_cell is None:
                print("No valid moves for black. Turn skipped.")
            else:
                game.flip_the_cell('black', new_cell)
                game.print_board()

            new_cell_white = game.select_random('white')
            if new_cell_white is None:
                print("No valid moves for white. Turn skipped.")
            else:
                game.flip_the_cell('white', new_cell_white)
                game.print_board()

            black_moves = game.set_the_available_move('black')
            white_moves = game.set_the_available_move('white')
            if not black_moves and not white_moves:
                print("No available moves for both players. Game over!")
                self.count_pieces()  
                break

    def play_game3(self):
        while True:
            black_moves = self.set_the_available_move('black')
            white_moves = self.set_the_available_move('white')

            if not black_moves and not white_moves:
                print("No available moves for both players. Game over!")
                self.count_pieces()  
                break

            if black_moves:
                new_cell = self.select_random('black')
                self.flip_the_cell('black', new_cell)
                self.print_board()
            else:
                print("No available moves for black. Turn skipped.")

            if white_moves:
                new_cell_white = self.select_random('white')
                self.flip_the_cell('white', new_cell_white)
                self.print_board()
            else:
                print("No available moves for white. Turn skipped.")
    def count_pieces(self):
        black_count = sum(row.count('black') for row in self.board)
        white_count = sum(row.count('white') for row in self.board)

        print(f"Final Score:")
        print(f"Black: {black_count}")
        print(f"White: {white_count}")

        if black_count > white_count:
            print("Black wins!")
        elif white_count > black_count:
            print("White wins!")
        else:
            print("It's a tie!")


game = ReversyGame()
game_type = game.start_game()
game.print_board()
if game_type == '1':
    game.play_game1()
elif game_type == '2':
    game.play_game2()
elif game_type == '3':
    game.play_game3()
else:
    print("error")

