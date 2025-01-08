# Node sınıfı tanımı
class GamePlayTree:
    def __init__(self, parent=None, depth=0, board=None, opponent_available_moves=None):
        self.parent = parent  # Node'un parent'ı
        self.children = []  # Node'un çocukları
        self.depth = depth  # Node'un depth'i
        self.board = board if board else [['' for _ in range(8)] for _ in range(8)]  # Board şeması
        self.opponent_available_moves = opponent_available_moves  # Rakibin mevcut hareketleri

    def add_child(self, child_node):
        child_node.parent = self  # Çocuğun parent'ını bu node olarak ayarla
        child_node.depth = self.depth + 1  # Çocuğun depth'ini hesapla
        self.children.append(child_node)  # Bu node'a çocuğu ekle

# Tahtayı ve ağacı yazdırma fonksiyonu
def print_tree(node, level=0):
    print("  " * level + f"Node Depth: {node.depth}")
    print("  " * level + "Board:")
    for row in node.board:
        print("  " * level + ' '.join(cell if cell else '.' for cell in row))
    print("  " * level + f"Opponent Available Moves: {node.opponent_available_moves}")
    print("  " * level + f"Number of Children: {len(node.children)}")
    print("\n")
    for child in node.children:
        print_tree(child, level + 1)
