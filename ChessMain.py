import pygame as p
import ChessEngine

WIDTH=HEIGHT=512
DIMENSION=8
SQ_SIZE=HEIGHT//DIMENSION
MAX_FPS=15
IMAGES={}

def loadImages():
    pieces=["wR","wN","wB","wQ","wK","wB","wN","wR","wp","bR","bN","bB","bQ","bK","bB","bN","bR","bp"]
    for piece in pieces:
       IMAGES[piece]=p.transform.scale(p.image.load("chess/images/" + piece + ".png"),(SQ_SIZE,SQ_SIZE))
       
def main():
    p.init()
    screen=p.display.set_mode((WIDTH,HEIGHT))
    clock=p.time.Clock()
    screen.fill(p.Color("white"))
    gs=ChessEngine.GameState()
    #print(gs.board)
    loadImages()
    running=True
    sqSelected=()
    playerClick=[]
    while running:
        for e in p.event.get():
            if e.type==p.QUIT:
                running=False
            elif e.type == p.MOUSEBUTTONDOWN:
               location = p.mouse.get_pos()
               col=location[0]//SQ_SIZE
               row =location[1]//SQ_SIZE
               if sqSelected == (row , col):
                  sqSelected=()
                  playerClick=[]
               else:
                  sqSelected= row,col   
                  playerClick.append(sqSelected)
               if len(playerClick) == 2:
                  move=ChessEngine.Move(playerClick[0],playerClick[1],gs.board)
                  print(move.getChessNotation())
                  gs.makeMove(move)
                  sqSelected=()
                  playerClick=[]


        drawGameState(screen ,gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen , gs):
    drawBoard(screen)
    drawPieces(screen , gs.board)
    
#def drawBoard(screen):
#    colors=[p.Color("white"),p.Color("gray")]
#    for r in range(DIMENSION):
#        for c in range(DIMENSION):
#            color=colors[((r+c)%2)]
#            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE , r*SQ_SIZE , SQ_SIZE , SQ_SIZE))

def drawBoard(screen):
    colors=[p.Color("white"),p.Color("gray")]
    for r in range(DIMENSION):
      for c in range(DIMENSION):
          color=colors[((r+c)%2)]
          #print(color)
          p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))



def drawPieces(screen,gs):

    #pieces=loadImages()
    for r in range(DIMENSION):
        for c in range(DIMENSION):
         piece=gs[r][c]
         if piece != "--":            
          #print(piece)
          screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
  
    

if __name__ == "__main__":
  main()






    

