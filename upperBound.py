from scipy.special import comb
import math

def chessCount():
    total = 0
    total2 = 0
    finalTotal = 0
    for t in range(0,16+1):
        pawnCount = (-abs(t-8)+9)
        pawnSquares = comb(48,t)
        for x in range(0,16-t+1):
            promotionCount = comb(x+3,3)
            for y in range(0,14+1):
                for z in range(0,6+1):
                    pieceSquares = comb(64-t,x+y+z+2)
                    placement = math.factorial(t+x+y+z+2)
                    pieceCount = comb(6,z)*comb(8-z,y)
                    total += pieceSquares * placement * pieceCount
            total2 += total*promotionCount
        finalTotal += total2*pawnCount*pawnSquares
    print(finalTotal)

chessCount()

# Output: 3.0697566281670323e+63
