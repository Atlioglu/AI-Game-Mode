
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
    
    def flip_the_cell(self, color,new_cell, future):
        temp_board = [row[:] for row in self.board]
        if future==1:
            board_act = temp_board
        else:
            board_act = self.board
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
        

        board_act[x_new][y_new] = color
        opponent_color = 'white' if color == 'black' else 'black'
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        for dx, dy in directions:
            x, y = x_new + dx, y_new + dy
            cells_to_flip = []

            while self.is_valid_position(x, y):
                if board_act[x][y] == opponent_color:
                    cells_to_flip.append((x, y))
                elif board_act[x][y] == color:
                    for cx, cy in cells_to_flip:
                        board_act[cx][cy] = color
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
            
            self.flip_the_cell(color, new_cell,1)
            number_of_cells = self.count_numbers(color)
            opponent_available_moves = self.set_the_available_move(opponent_color)

            future_moves_map[new_cell] = {
                "number_of_cells": number_of_cells,
                "opponent_available_moves": opponent_available_moves
            }
            #self.undo()

        return future_moves_map

    def count_numbers(self, color):
        count = sum(row.count(color) for row in self.board)
        return count
    
    def undo(self):
        
        self.board = [row[:] for row in self.previous_board]


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


    
    def update_tree(self, root, color, depth_limit=3):
        """
        Ağacı günceller ve belirtilen depth_limit'e kadar çocuk düğümleri oluşturur.
        Args:
            root (GamePlayTree): Başlangıç root düğümü.
            color (str): Oynayan oyuncunun rengi ('black' veya 'white').
            depth_limit (int): Ağacın oluşturulacağı maksimum derinlik.
        Returns:
            GamePlayTree: Güncellenmiş root düğümü.
        """
        def create_children(node, current_depth, current_color):
            if current_depth >= depth_limit:
                return

            # Mevcut düğüm için geçerli hamleleri al
            available_moves = self.set_the_available_move(current_color)
            opponent_color = 'white' if current_color == 'black' else 'black'

            for move in available_moves:
                # Yeni tahtayı hesapla
                new_board = [row[:] for row in node.board]  # Mevcut düğümün tahtasını kopyala
                self.board = new_board
                self.flip_the_cell(current_color, move, future=1)

                # Yeni bir child düğümü oluştur
                child_node = GamePlayTree(
                    parent=node,
                    depth=current_depth + 1,
                    board=[row[:] for row in self.board],  # Yeni tahtayı kopyala
                    opponent_available_moves=self.set_the_available_move(opponent_color)
                )
                node.add_child(child_node)

                # Çocuk için aynı işlemi uygula
                create_children(child_node, current_depth + 1, opponent_color)

        # Root'tan başla ve çocukları oluştur
        create_children(root, root.depth, color)
        return root

