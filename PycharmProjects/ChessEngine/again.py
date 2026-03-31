class Board:
    def __init__(self):
        self.board=[["--" for j in range(8)]for i in range(8)]
        self.board[0]=["wR","wN","wB","wQ","wK","wB","wN","wR"]
        self.board[1] =["wP","wP","wP","wP","wP","wP","wP","wP"]
        self.board[6]=["bR","bN","bB","bQ","bK","bB","bN","bR"]
        self.board[7] =["bP","bP","bP","bP","bP","bP","bP","bP"]
    def display(self):
        for i in range(8):
            for j in range(8):
                print(self.board[i][j],end=" ")
            print()
    def move(self,from_row,from_col,to_row,to_col):
        piece = self.board[from_row][from_col]
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = "--"

c=Board()
c.display()
c.move(1, 0, 2, 0)

c.display()