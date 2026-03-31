class Board:
    def __init__(self):
        self.board=[["--" for j in range(8)] for i in range(8)]
        self.board[0] = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
        self.board[1]=["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"]
        self.board[6]=["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"]
        self.board[7]=["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    def display(self):
      for i in range(8):
          for j in range(8):
            print(self.board[i][j],end=" ")
          print()


chess = Board()
chess.display()