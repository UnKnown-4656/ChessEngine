class GameState:
    def __init__(self):
        self.board=[
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        self.WhiteToMove=True
        self.movelog=[]
    def makeMove(self ,Move):
        self.board[Move.startRow][Move.startCol]="--"
        self.board[Move.endRow][Move.endCol]=Move.pieceMoved
        self.movelog.append(Move)
        self.WhiteToMove=not self.WhiteToMove


class Move:
    ranksToRows={"1":7,"2":6,"3":5,"4":4,
                "5":3,"6":2,"7":1,"8":0}
    
    filesToCols={"a":0,"b":1,"c":2,"d":3,
                 "e":4,"f":5,"g":6,"h":7
                 }
    rowsToRanks = {v:k for k ,v in filesToCols.items()}
    closToFiles ={v:k for k,v in filesToCols.items()}

    def __init__(self,startSq,endSq,board):
        self.startRow=startSq[0]
        self.startCol=startSq[1]
        self.endRow=endSq[0]
        self.endCol=endSq[1]
        self.pieceMoved=board[self.startRow][self.startCol]
        self.pieceCaptured=board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankFiles(self.startRow,self.startCol)+self.getRankFiles(self.endRow,self.endCol)
    
    def getRankFiles(self ,r ,c):
        return self.closToFiles[c]+self.rowsToRanks[r]
