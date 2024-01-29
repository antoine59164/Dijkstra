def createMatrix(rowCount, colCount, dataList):
    matrix = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            rowList.append(dataList[rowCount * i + j])
        matrix.append(rowList)

    return matrix


def find(summits: [], values):
    for x in summits:
        if x.name == values:
            return x
