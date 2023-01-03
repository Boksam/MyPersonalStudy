import random
import math


class Problem:
    def __init__(self):
        self._solution = []
        self._value = 0
        self._numEval = 0

    def setVariables(self): # n&tsp
        pass

    def randomInit(self):   # n&tsp
        pass

    def evaluate(self):
        pass

    def mutants(self):  # steepest Ascent
        pass

    def randomMutant(self, current):    # first-choice
        pass

    def describe(self):
        pass

    def storeResult(self, solution, value):
        self._solution = solution
        self._value = value

    def report(self):
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))


class Numeric(Problem):
    def __init__(self):
        Problem.__init__(self)
        self._expression = ''
        self._domain = []
        self._delta = 0.01

        self._alpha = 0.01
        self._dx = 10 ** (-4)

    def setVariables(self):
        fileName = input('Enter file name of numeric :')
        infile = open(fileName, 'r')
        
        self._expression = infile.readline()
        
        varNames = []
        low = []
        up = []

        line = infile.readline()
        while line != '':
            data = line.split(',')
            varNames.append(data[0])
            low.append(float(data[1]))
            up.append(float(data[2]))
            line = infile.readline()
        infile.close()

        self._domain = [varNames, low, up]

    def getDelta(self):
        return self._delta

    def getAlpha(self):     # gradient descent
        return self._alpha

    def getDx(self):        # gradient descent
        return self._dx

    def randomInit(self):   # All
        domain = self._domain
        low, up = domain[1], domain[2]

        init = []
        for i in range(len(low)):
            r = random.uniform(low[i], up[i])
            init.append(r)
        return init

    def evaluate(self, current):    # All
        self._numEval += 1

        varNames = self._domain[0]
        for i in range(len(current)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
        return eval(self._expression)

    def mutants(self, current): # Steepest-Ascent
        neighbors = []
        
        for i in range(len(current)):
            mutant = self.mutate(current, i, self._delta)
            neighbors.append(mutant)
            mutant = self.mutate(current, i, -self._delta)
            neighbors.append(mutant)
        return neighbors

    def mutate(self, current, i, d):    
        curCopy = current[:]
        low, up = self._domain[1][i], self._domain[2][i]
        if low <= (curCopy[i] + d) <= up:
            curCopy[i] += d
        return curCopy

    def randomMutant(self, current):    # first-choice
        i = random.randint(0, len(current) - 1)
        if random.uniform(0, 1) > 0.5:
            d = self._delta
        else:
            d = -self._delta
        return self.mutate(current, i, d)

    def takeStep(self, x, v):   # gradient descent
        grad = self.gradient(x, v)
        xCopy = x[:]
        for i in range(len(xCopy)):
            xCopy[i] = xCopy[i] - self._alpha * grad[i]
        if self.isLegal(xCopy):
            return xCopy
        else:
            return x

    def gradient(self, x, v):
        grad = []
        for i in range(len(x)):
            xCopyH = x[:]
            xCopyH[i] += self._dx
            g = (self.evaluate(xCopyH) - v) / self._dx
            grad.append(g)
        return grad
        
    def isLegal(self, x):
        domain = self._domain
        low = domain[1]
        up = domain[2]
        flag = True

        for i in range(len(low)):
            if x[i] < low[i] or x[i] > up[i]:
                flag = False
                break
        return flag

    def describe(self):
        print()
        print("Objective function:")
        print(self._expression)
        print("Search space:")
        varNames = self._domain[0] # domain: [VarNames, low, up]
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(low)):
            print(" " + varNames[i] + ":", (low[i], up[i]))

    def report(self):
        print()
        print("Solution found:")
        print(self.coordinate())  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(self._value))
        Problem.report(self)

    def coordinate(self):
        c = [round(value, 3) for value in self._solution]
        return tuple(c)  # Convert the list to a tuple


class Tsp(Problem):
    def __init__(self):
        Problem.__init__(self)
        self._numCities = 0
        self._locations = []
        self._distanceTable = []

    def setVariables(self):
        fileName = input('Enter file name of Tsp :')
        infile = open(fileName, 'r')
        
        self._numCities = int(infile.readline())

        cityLocs = []
        line = infile.readline()
        while line != '':
            cityLocs.append(eval(line))
            line = infile.readline()
        infile.close()
        
        self._locations = cityLocs
        self._distanceTable = self.calcDistanceTable()

    def calcDistanceTable(self):
        locations = self._locations
        table = []
        for i in range(self._numCities):
            row = []
            for j in range(self._numCities):
                dx = locations[i][0] - locations[j][0]
                dy = locations[i][1] - locations[j][1]
                distance = round(math.sqrt(dx**2 + dy**2), 1)
                row.append(distance)
            table.append(row)
        return table

    def randomInit(self):
        n = self._numCities
        init = list(range(n))
        random.shuffle(init)
        return init

    def evaluate(self, current):
        self._numEval += 1
        n = self._numCities
        table = self._distanceTable
        cost = 0

        for i in range(n - 1):
            locFrom = current[i]
            locTo = current[i + 1]
            cost += self._distanceTable[locFrom][locTo]
        return cost

    def mutants(self, current):     # steepestAscent 
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = []

        while count <= n:
            i, j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                count += 1
                mutant = self.inversion(current, i, j)
                neighbors.append(mutant)
        return neighbors

    def inversion(self, current, i, j):
        mutant = current[:]
        while i < j:
            mutant[i], mutant[j] = mutant[j], mutant[i]
            i += 1
            j -= 1
        return mutant

    def randomMutant(self, current):
        while True:
            i, j = sorted([random.randrange(self._numCities) for _ in range(2)])
            if i < j:
                mutant = self.inversion(current, i, j)
                break
        return mutant

    def describe(self):
        print()
        n = self._numCities
        print("Number of cities:", n)
        print("City locations:")
        locations = self._locations
        for i in range(len(self._locations)):
            print(i, ':', self._locations[i])

        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end = '')
            if i % 5 == 4:
                print()

    def report(self):
        print()
        print("Best order of visits:")
        self.tenPerRow()  # Print 10 cities per row
        print("Minimum tour cost: {0:,}".format(round(self._value)))
        Problem.report(self)

    def tenPerRow(self):
        solution = self._solution
        for i in range(len(solution)):
            print("{0:>5}".format(solution[i]), end='')
            if i % 10 == 9:
                print()

