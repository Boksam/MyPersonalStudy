import random
import math

"""
[Problem] class is complete as it is.
Do not need to modify!!!
"""
class Problem:
    def __init__(self):
        self._solution = []
        self._value = 0
        self._numEval = 0

    def setVariables(self):
        pass
    
    def randomInit(self):
        pass

    def evaluate(self):
        pass

    def mutants(self):
        pass

    def randomMutant(self, current):
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
        self._domain = []     # domain as a list
        self._delta = 0.01    # Step size for axis-parallel mutation

        self._alpha = 0.01    # Update rate for gradient descent
        self._dx = 10 ** (-4) # Increment for calculating derivative
    
    def setVariables(self):
        ###
        ### Your code goes here!
        ### note: code here should be almost the same as 
        ###       createProblem() you coded before
        ###
        fileName = input("Enter the file name of numeric :")
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

    def getAlpha(self):
        return self._alpha

    def getDx(self):
        return self._dx

    def randomInit(self): # Return a random initial point as a list
        ###
        ### Your code goes here!
        ###
        domain = self._domain
        low, up = domain[1], domain[2]
        init = []
        for i in range(len(low)):
            r = random.uniform(low[i], up[i])
            init.append(r)
        return init

    def evaluate(self, current):
        ###
        ### Your code goes here!
        ###
        self._numEval += 1
        varNames = self._domain[0]
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
        return eval(self._expression)

    def mutants(self, current):
        ###
        ### Your code goes here!
        ###
        neighbors = []
        for i in range(len(current)):
            mutant = self.mutate(current, i, self._delta)
            neighbors.append(mutant)
            mutant = self.mutate(current, i, -self._delta)
            neighbors.append(mutant)
        return neighbors

    def mutate(self, current, i, d): ## Mutate i-th of 'current' if legal
        ###
        ### Your code goes here!
        ###
        mutant = current[:]
        domain = self._domain
        l = domain[1][i]
        u = domain[2][i]
        if l <= (mutant[i] + d) <= u:
            mutant[i] += d
        return mutant

    def randomMutant(self, current):
        ###
        ### Your code goes here!
        ###
        i = random.randint(0, len(current) - 1)
        if random.uniform(0, 1) > 0.5:
            d = self._delta
        else:
            d = -self._delta
        return self.mutate(current, i, d)

    def takeStep(self, x, v): # Take gradient and make update if legal
        grad = self.gradient(x, v)
        xCopy = x[:]
        for i in range(len(xCopy)):
            xCopy[i] = xCopy[i] - self._alpha * grad[i]
        if self.isLegal(xCopy):
            return xCopy
        else:
            return x

    def gradient(self, x, v): # 'x' is a vector (list of valules)
        grad = []   # Calculate partial derivatives and combine them
        for i in range(len(x)):
            xCopyH = x[:]
            xCopyH[i] += self._dx
            g = (self.evaluate(xCopyH) - v) / self._dx
            grad.append(g)
        return grad

    def isLegal(self, x):   # Check if 'x' is within the domain
        domain = self._domain
        low = domain[1]
        up = domain[2]
        flag = True
        for i in range(len(low)):
            if x[i] < low[i] or up[i] < x[i]:
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
        self._locations = []       # A list of tuples
        self._distanceTable = []

    def setVariables(self):
        ###
        ### Your code goes here!
        ### note: code here should be almost the same as 
        ###       createProblem() before
        ###
        fileName = input("Enter file name of Tsp :")
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
        ###
        ### Your code goes here!
        ###
        locations = self._locations
        table = []
        for i in range(self._numCities):
            row = []
            for j in range(self._numCities):
                dx = locations[i][0] - locations[j][0]
                dy = locations[i][1] - locations[j][1]
                d = round(math.sqrt(dx**2 + dy**2), 1)
                row.append(d)
            table.append(row)
        return table

    def randomInit(self):   # Return a random initial tour
        ###
        ### Your code goes here!
        ###
        n = self._numCities
        init = list(range(n))
        random.shuffle(init)
        return init

    def evaluate(self, current):
        ###
        ### Your code goes here!
        ###
        self._numEval += 1
        n = self._numCities
        table = self._distanceTable
        cost = 0
        for i in range(n - 1):
            locFrom = current[i]
            locTo = current[i+1]
            cost += table[locFrom][locTo]
        return cost

    def mutants(self, current): # Inversion only
        ###
        ### Your code goes here!
        ###
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = []
        while count <= n:
            i, j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                mutant = self.inversion(current, i, j)
                count += 1
                neighbors.append(mutant)
        return neighbors
            

    def inversion(self, current, i, j):  ## Perform inversion
        ###
        ### Your code goes here!
        ###
        mutant = current[:]
        while i < j:
            mutant[i], mutant[j] = mutant[j], mutant[i]
            i += 1
            j -= 1
        return mutant

    def randomMutant(self, current): # Inversion only
        ###
        ### Your code goes here!
        ###
        while True:
            i, j = sorted([random.randrange(self._numCities) for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)
                break
        return curCopy


    def describe(self):
        print()
        n = self._numCities
        print("Number of cities:", n)
        print("City locations:")
        locations = self._locations
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

