import numpy as np


def main():
    print("Which learning algorithm do you want to use?")
    print(" 1. Linear Regression")
    print(" 2. k-NN")
    aType = int(input("Enter the number: "))
    if aType == 1:
        ml = LinearRegression()
    elif aType == 2:
        ml = KNN()
    ml.setAType(aType)  # set aType

    fileName = input("Enter the file name of training data: ")
    ml.setData("train", fileName)
    fileName = input("Enter the file name of test data: ")
    ml.setData("test", fileName)
    ml.buildModel()
    ml.testModel()
    ml.report()


class ML:
    def __init__(self):
        self._trainDX = np.array([])  # Feature value matrix (training data)
        self._trainDy = np.array([])  # Target column (training data)
        self._testDX = np.array([])  # Feature value matrix (test data)
        self._testDy = np.array([])  # Target column (test data)
        self._testPy = np.array([])  # Predicted values for test data

        self._rmse = 0  # Root mean squared error
        self._aType = 0  # Type of learning algoritm

    def setAType(self, aType):  # setter
        self._aType = aType

    def setData(self, dtype, fileName):  # set class variables
        XArray, yArray = self.createMatrices(fileName)  # x와 y의 어레이 생성
        if dtype == "train":
            self._trainDX = XArray
            self._trainDy = yArray
        elif dtype == "test":
            self._testDX = XArray
            self._testDy = yArray
            self._testPy = np.zeros(np.size(yArray))  # Initialize to all 0

    def createMatrices(self, fileName):  # Read data from file and make arrays
        infile = open(fileName, "r")
        XSet = []
        ySet = []
        for line in infile:
            data = [float(x) for x in line.split(",")]
            features = data[0:-1]
            target = data[-1]
            XSet.append(features)
            ySet.append(target)
        infile.close()
        XArray = np.array(XSet)
        yArray = np.array(ySet)
        return XArray, yArray

    def testModel(self):
        n = np.size(self._testDy)
        if self._aType == 1:
            self.testLR(n)
        elif self._aType == 2:
            self.testKNN(n)

    def testKNN(self, n):  # Apply k-NN to the test set
        for i in range(n):
            self._testPy[i] = self.runModel(self._testDX[i])

    def testLR(self, n):  # Test linear regression with the test set
        for i in range(n):
            self._testPy[i] = self.runModel(self._testDX[i])

    def report(self):
        self.calcRMSE()
        print()
        print("RMSE: ", round(self._rmse, 2))

    def calcRMSE(self):
        n = np.size(self._testDy)  # Number of test data
        totalSe = 0
        for i in range(n):
            se = (self._testDy[i] - self._testPy[i]) ** 2
            totalSe += se
        self._rmse = np.sqrt(totalSe) / n


class LinearRegression(ML):
    def __init__(self):
        ML.__init__(self)
        self._w = np.array([])  # Optimal weights for linear regression
        # 해당 클래스 영역에서만 쓰이는 멤버변수

    def buildModel(self):  # Do linear regression and return optimal w
        # 기존의 linearRegression 함수사용
        X = self._trainDX
        n = np.size(self._trainDy)
        X0 = np.ones([n, 1])
        nX = np.hstack((X0, X))  # Add a column of all 1's as the first column
        y = self._trainDy
        t_nX = np.transpose(nX)
        # 결과값을 멤버변수에 저장
        self._w = np.dot(np.dot(np.linalg.inv(np.dot(t_nX, nX)), t_nX), y)

    def runModel(self, data):  # Apply linear regression to a test data
        # 기존의 LR 함수 사용
        nData = np.insert(data, 0, 1)
        return np.inner(self._w, nData)


class KNN(ML):
    def __init__(self) -> None:
        ML.__init__(self)
        self._k = 0

    def buildModel(self):
        self._k = int(input("Enter the value for k: "))

    def runModel(self, query):
        closestK = self.findCK(query)
        predict = self.takeAvg(closestK)
        return predict

    def findCK(self, query):
        m = np.size(self._trainDy)
        k = self._k
        closestK = np.arange(2 * k).reshape(k, 2)
        for i in range(k):
            closestK[i, 0] = i
            closestK[i, 1] = self.sDistance(self._trainDX[i], query)
        for i in range(k, m):
            self.updateCK(closestK, i, query)
        return closestK

    def sDistance(self, dataA, dataB):
        dim = np.size(dataA)
        sumOfSquares = 0
        for i in range(dim):
            sumOfSquares += (dataA[i] - dataB[i]) ** 2
        return sumOfSquares

    def updateCK(self, closestK, i, query):
        d = self.sDistance(self._trainDX[i], query)

        j = np.argmax(closestK[:, 1])
        if closestK[j, 1] > d:
            closestK[j, 0] = i
            closestK[j, 1] = d

    def takeAvg(self, closestK):
        k = self._k
        total = 0
        for i in range(k):
            j = closestK[i, 0]
            total += self._trainDy[j]
        return total / k


main()
