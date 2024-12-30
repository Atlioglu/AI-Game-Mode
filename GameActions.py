class GameActions:
    def __init__(self, board):
        self.board = board
        self.previous_board = [row[:] for row in self.board]  # Derin kopya oluştur

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
    
    def flip_the_cell(self, color,new_cell):
        self.previous_board = [row[:] for row in self.board]
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
    
    def future_moves(self, color):
        opponent_color = 'black' if color == 'white' else 'white'
        available_moves = self.set_the_available_move(color)
        future_moves_map = {}

        for new_cell in available_moves:
            self.flip_the_cell(color, new_cell)
            number_of_cells = self.count_numbers(color)
            opponent_available_moves = self.set_the_available_move(opponent_color)

            future_moves_map[new_cell] = {
                "number_of_cells": number_of_cells,
                "opponent_available_moves": opponent_available_moves
            }

            self.undo()

        return future_moves_map

    def count_numbers(self, color):
        count = sum(row.count(color) for row in self.board)
        return count
    
    def undo(self):
        """
        Son yapılan hamleyi geri alır ve tahtayı önceki duruma döndürür.
        """
        self.board = [row[:] for row in self.previous_board]
    


