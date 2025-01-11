import random
from GameActions import GameActions

class Algorithms:
    def __init__(self, actions):
        self.actions = actions

    def play_each_other(self, color):
        available_moves = self.actions.set_the_available_move(color,self.actions.board)
        if not available_moves:
            print(f"No available moves for {color}. Turn skipped.")
            return None
        while True:
            try:
                user_input = input(f"Enter your move for {color} (row, column) or 'q' to quit, 'h' for the hint: ").strip()
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



    def select_greedy(self, color):
        future_moves = self.actions.future_moves(color)
        best_move = max(future_moves.items(), key=lambda item: item[1]['number_of_cells'])
        print(f"The best move selected for {color}: {best_move[0]}")
        return best_move[0]

    def select_the_prevented(self, color):
        corners = {(0, 0), (0, 7), (7, 0), (7, 7)}
        edges = {
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
            (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6),
            (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7)
        }

        # Get future moves for the color
        future_moves = self.actions.future_moves(color)

        for key, value in future_moves.items():
            decision_value = value['number_of_cells']

            for move in value['opponent_available_moves']:
                if move in corners:
                    decision_value -= 3
                elif move in edges:
                    decision_value -= 1

            if key in corners:
                decision_value += 4
            elif key in edges:
                decision_value += 1

            value['decision_value'] = decision_value

        # Select the key with the highest decision_value
        best_move = max(future_moves.items(), key=lambda item: item[1]['decision_value'])
        print(f"The best move selected for {color}: {best_move[0]} with decision_value: {best_move[1]['decision_value']}")
        return best_move[0]


    def select_corner_or_edge(self, color):
        available_moves = self.actions.set_the_available_move(color,self.actions.board)
        if not available_moves:
            print(f"No available moves for {color}.")
            return None

        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        corner_moves = [move for move in available_moves if move in corners]
        if corner_moves:
            selected_move = random.choice(corner_moves)
            print(f"Corner move selected for {color}: {selected_move}")
            return selected_move

        edge_moves = [move for move in available_moves if move[0] in {0, 7} or move[1] in {0, 7}]
        if edge_moves:
            selected_move = random.choice(edge_moves)
            print(f"Edge move selected for {color}: {selected_move}")
            return selected_move

        random_move = random.choice(available_moves)
        print(f"Randomly selected move for {color}: {random_move}")
        return random_move
    

    def select_the_best_move_with_edges(self, color):
        corners = {(0, 0), (0, 7), (7, 0), (7, 7)}
        edges = {
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
            (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6),
            (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7)
        }

        danger_zone = {
            (0, 1), (1, 1), (1, 0),
            (0, 6), (1, 6), (1, 7),
            (6, 0), (6, 1), (7, 1),
            (7, 6), (6, 6), (6, 7)
        }

        # Map each danger zone cell to its nearest corner
        danger_zone_to_corner = {
            (0, 1): (0, 0), (1, 1): (0, 0), (1, 0): (0, 0),
            (0, 6): (0, 7), (1, 6): (0, 7), (1, 7): (0, 7),
            (6, 0): (7, 0), (6, 1): (7, 0), (7, 1): (7, 0),
            (7, 6): (7, 7), (6, 6): (7, 7), (6, 7): (7, 7)
        }

        # Get future moves for the color
        future_moves = self.actions.future_moves(color)

        occupied_corners = {corner for corner in corners if self.actions.board[corner[0]][corner[1]] == color}

        for key, value in future_moves.items():
            decision_value = value['number_of_cells']

            for move in value['opponent_available_moves']:
                if move in corners:
                    decision_value -= 4
                elif move in edges:
                    decision_value -= 1

            if key in corners:
                decision_value += 5
            elif key in edges:
                decision_value += 1

            for corner in occupied_corners:
                if corner[0] == 0 and key[0] == 0 or corner[1] == 0 and key[1] == 0:
                    decision_value += 2
                elif corner[0] == 7 and key[0] == 7 or corner[1] == 7 and key[1] == 7:
                    decision_value += 2
        #    Check danger zone condition
            if key in danger_zone:
                nearest_corner = danger_zone_to_corner[key]
                if nearest_corner not in occupied_corners:
                    decision_value -= 5
            value['decision_value'] = decision_value

        # Select the keys with the highest decision_value
        max_decision_value = max(value['decision_value'] for value in future_moves.values())
        best_moves = [key for key, value in future_moves.items() if value['decision_value'] == max_decision_value]

        # Choose randomly among the best moves if there's a tie
        best_move = random.choice(best_moves)
        print(f"The best move selected for {color}: {best_move} with decision_value: {future_moves[best_move]['decision_value']}")
        return best_move
    



    @staticmethod
    def minimax_function(tree, color):
        def count_color(board, color):
            return sum(row.count(color) for row in board)
        def minimax(node, maximizing_player):
            if not node.children:  # Leaf node
                return count_color(node.board, color)

            if maximizing_player:
                value = float('-inf')
                for child in node.children:
                    value = max(value, minimax(child, False))
                return value
            else:
                opponent_color = 'black' if color == 'white' else 'white'
                value = float('inf')
                for child in node.children:
                    value = min(value, minimax(child, True))
                return value

        best_value = float('-inf')
        best_move = None
        for child in tree.children:
            child_value = minimax(child, False)
            if child_value > best_value:
                best_value = child_value
                best_move = child

        return best_move, best_value
