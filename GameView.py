class GameView:
    def __init__(self, board):
        self.board = board

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
