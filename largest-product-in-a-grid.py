import numpy as np


inputMat = np.loadtxt("euler11Data.txt", dtype=int, delimiter=" ")
nRows, nCols = inputMat.shape
nAdjNums = 4  # n adjacent numbers
largestProduct = 0

for i in range(nRows):
    for j in range(nCols-nAdjNums+1):
        # horizontal nAdjNums product
        hProd = np.prod(inputMat[i, j:j+nAdjNums], dtype=int)
        # hProdList.append(hProd)
        vProd = np.prod(inputMat[j, i:i+nAdjNums], dtype=int)
        # vProdList.append(vProd)
        if hProd > largestProduct:
            largestProduct = hProd
        # vertical nAdjNums product
        if vProd > largestProduct:
            largestProduct = vProd

for i in range(nRows-nAdjNums+1):
    for j in range(nCols-nAdjNums+1):
        # north-west to south east diag
        nwToSeDiagProd = 1
        # north east to south west diag
        neToSwDiagProd = 1
        nextI = range(i, i+nAdjNums)
        nextJ = range(j, j+nAdjNums)
        nwToSeDiagProd = inputMat[nextI, nextJ].prod()
        neToSwDiagProd = inputMat[nextI, nextJ[::-1]].prod()

        if nwToSeDiagProd > largestProduct:
            largestProduct = nwToSeDiagProd
        if neToSwDiagProd > largestProduct:
            largestProduct = neToSwDiagProd
print(largestProduct)
# 70600674
