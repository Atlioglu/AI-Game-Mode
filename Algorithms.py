import random
from GameActions import GameActions

class Algorithms:
    def __init__(self, actions):
        self.actions = actions

    def play_each_other(self, color):
        available_moves = self.actions.set_the_available_move(color)
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

    def select_random(self, color):
        available_moves = self.actions.set_the_available_move(color)
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
