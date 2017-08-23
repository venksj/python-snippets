from numpy import *
import operator


def createDataSet():
    group  = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]]) # 4X2
    labels =    ['A', 'A', 'B', 'B']

    return group, labels


def getDistances(inX, dataSet):
    print ("DataSet: ")
    print (dataSet)

    rowSize = dataSet.shape[0]  # get rowSize from dataSet

    tileMat = tile(inX, (rowSize, 1))
    print ("Tile of inX: ")
    print (tileMat)

    diffMat = tileMat - dataSet # first create matrix from inX. Then subtract dataSet from this matrix
    print ("Difference Matrix: ")
    print (diffMat)

    sqDiffMat = diffMat**2  # take the square of each element of the difference matrix
    print ("Square of Difference Matrix: ")
    print (sqDiffMat)

    sqDistances = sqDiffMat.sum(axis=1) # find the sum of the squares based on rows
    print ("Sum of squares of Difference Matrix: ")
    print (sqDistances)

    distances = sqDistances**0.5 # sq root
    print ("Square Root of Difference Matrix: ")
    print (distances)

    return distances


def computeFromTrainingSet(labels, sortedDist, k):
    classCount = {}
    for i in range(k):
        voteILabel = labels[sortedDist[i]]
        classCount[voteILabel] = classCount.get(voteILabel, 0) + 1

    return classCount


def classify0(inX, dataSet, labels, k):
    distances = getDistances(inX, dataSet)

    # now sort
    sortedDist = distances.argsort()
    print ("Sorted distances: ")
    print (sortedDist)

    classCount = computeFromTrainingSet(labels, sortedDist, k)
    print ("classCount: ")
    print (classCount)

    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    print ("Sorted classCount: ")
    print (sortedClassCount)

    return sortedClassCount[0][0]

