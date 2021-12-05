import numpy as np

def langtonAnt(width, height):
    antBoard = np.full((width, height), False, dtype=bool)
    # first ant's coordinate: center of board
    x, y = width//2, height//2
    # e^(i*pi/2) = i --> rotate 90 degrees
    # e^(-i*pi/2) = -i --> rotate -90 degrees
    direction = complex(0, 1)
    for _ in range(10**6):
        if x in range(0, width) and y in range(0, height):
            if antBoard[x, y]:
                direction *= complex(0, 1)
            else:
                direction *= complex(0, -1)
            antBoard[x, y] = not antBoard[x, y]
            nextAntCoord = complex(x, y) + direction
            x, y = int(nextAntCoord.real), int(nextAntCoord.imag)
        else:
            break
    return antBoard

width = 200
height = 200
antBoard = langtonAnt(width, height)
with open("langtonAnt.txt", "w") as antBoardFile:
    for i in range(width):
        for j in range(height):
            if antBoard[i, j]:
                antBoardFile.write("*")
            else:
                antBoardFile.write(".")
        antBoardFile.write("\n")
