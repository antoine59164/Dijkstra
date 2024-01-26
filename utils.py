def createMatrix(rowCount, colCount, dataList):
    matrix = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            rowList.append(dataList[rowCount * i + j])
        matrix.append(rowList)

    return matrix
