class GamePlayTree:
    def __init__(self, parent=None, depth=0, board=None, opponent_available_moves=None):
        self.parent = parent  
        self.children = []  
        self.depth = depth  
        self.board = board if board else [['' for _ in range(8)] for _ in range(8)]  
        self.opponent_available_moves = opponent_available_moves  

    def add_child(self, parent, child, number_of_cell, available_moves):
        child.parent = parent  
        child.depth = parent.depth + 1  
        child.opponent_available_moves = available_moves  
        parent.children.append(child)  