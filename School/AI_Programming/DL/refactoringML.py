import numpy as np

# KNN 7까지


def main():
    # 다운 캐스팅이 어려우니 어떤 알고리즘을 사용할 건지 먼저 선택
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

    # ML
    def setData(self, dtype, fileName):  # set class variables
        XArray, yArray = self.createMatrices(fileName)  # x와 y의 어레이 생성
        if dtype == "train":
            self._trainDX = XArray
            self._trainDy = yArray
        elif dtype == "test":
            self._testDX = XArray
            self._testDy = yArray
            self._testPy = np.zeros(np.size(yArray))  # Initialize to all 0

    # ML
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

    # ML
    def testModel(self):
        n = np.size(self._testDy)
        if self._aType == 1:
            self.testLR(n)
        elif self._aType == 2:
            self.testKNN(n)

    # ML
    def testKNN(self, n):  # Apply k-NN to the test set
        for i in range(n):
            self._testPy[i] = self.runModel(self._testDX[i])

    # ML
    def testLR(self, n):  # Test linear regression with the test set
        for i in range(n):
            self._testPy[i] = self.runModel(self._testDX[i])

    # ML
    def report(self):
        self.calcRMSE()
        print()
        print("RMSE: ", round(self._rmse, 2))

    # ML
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
        self._k = 0  # k value for k-NN
        # 해당 클래스에서 사용될 멤버변수
        # self.buildModel()
        # k 값을 여기서 초기화하면 더 깔끔할텐데

    # # KNN
    def buildModel(self):  # k를 사용자로부터 입력받는 함수
        self._k = int(input("Enter the value for k: "))

    ### Implement the following and other necessary methods
    def runModel(self, query):
        closestK = self.findCK(query)
        predict = self.takeAvg(closestK)
        return predict

    # KNN
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

    # KNN
    def sDistance(self, dataA, dataB):
        dim = np.size(dataA)
        sumOfSquares = 0
        for i in range(dim):
            sumOfSquares += (dataA[i] - dataB[i]) ** 2
        return sumOfSquares

    # KNN
    def updateCK(self, closestK, i, query):
        d = self.sDistance(self._trainDX[i], query)

        j = np.argmax(closestK[:, 1])
        if closestK[j, 1] > d:
            closestK[j, 0] = i
            closestK[j, 1] = d

    # KNN
    def takeAvg(self, closestK):
        k = self._k
        total = 0
        for i in range(k):
            j = closestK[i, 0]
            total += self._trainDy[j]
        return total / k


main()
