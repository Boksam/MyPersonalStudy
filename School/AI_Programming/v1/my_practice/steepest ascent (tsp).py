import random
import math

NumEval = 0


def main():
    p = createProblem()

    solution, minimum = steepestAscent(p)

    describeProblem(p)
    displaySetting()
    displayResult(solution, minimum)

def createProblem():    # p : (numCities, locations, table)
    fileName = input("input file name :")
    infile = open(fileName, 'r')
    numCities = int(infile.readline())
    locations = []
    
    line = infile.readline()
    while line != '':
        locations.append(eval(line))
        line = infile.readline()
    infile.close()

    table = calcDistanceTable(numCities, locations)

    return numCities, locations, table


def calcDistanceTable(numCities, locations):
    table = []
    
    for i in range(numCities):
        row = []
        for j in range(numCities):
            dx = locations[i][0] - locations[j][0]
            dy = locations[i][1] - locations[j][1]
            distance = round(math.sqrt(dx**2 + dy**2), 1)
            row.append(distance)
        table.append(row)
    return table


def steepestAscent(p):
    current = randomInit(p)
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p)
        if valueC <= valueS:
            break
        else:
            current, valueC = successor, valueS
    return current, valueC

def randomInit(p):
    n = p[0]
    init = list(range(n))
    random.shuffle(init)
    return init

def evaluate(current, p):
    global NumEval
    NumEval += 1
    
    n = p[0]
    table = p[2]
    cost = 0
    for i in range(n - 1):
        locFrom = current[i]
        locTo = current[i + 1]
        cost += table[locFrom][locTo]
    return cost

def mutants(current, p):    # make mutant using inversion with size of numOfCities
    count = 0
    n = p[0]
    triedPairs = []
    
    neighbors = []

    while count <= n:
        i,j = sorted([random.randrange(n) for _ in range(2)])
        if i < j and [i, j] not in triedPairs:
            triedPairs.append([i,j])
            mutant = inversion(current, i, j)
            count += 1
            neighbors.append(mutant)
    return neighbors


def inversion(current, i, j):
    curCopy = current[:]
    while i < j:
        curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
        i += 1
        j -= 1
    return curCopy

def bestOf(neighbors, p):
    best = neighbors[0]
    bestValue = evaluate(best, p)
    for i in range(1, len(neighbors)):
        newValue = evaluate(neighbors[i], p)
        if newValue < bestValue:
            best = neighbors[i]
            bestValue = newValue
    return best, bestValue

def describeProblem(p):
    print()
    n = p[0]
    print("Number of cities:", n)
    print("City locations:")
    locations = p[1]
    for i in range(n):
        print("{0:>12}".format(str(locations[i])), end = '')
        if i % 5 == 4:
            print()

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")

def displayResult(solution, minimum):
    print()
    print("Best order of visits:")
    tenPerRow(solution)       # Print 10 cities per row
    print("Minimum tour cost: {0:,}".format(round(minimum)))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def tenPerRow(solution):
    for i in range(len(solution)):
        print("{0:>5}".format(solution[i]), end='')
        if i % 10 == 9:
            print()

main()