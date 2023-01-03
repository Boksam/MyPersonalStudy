import random
import math

LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement
NumEval = 0


def main():
    p = createProblem()

    solution, minimum = firstChoice(p)

    describeProblem(p)
    displaySetting()
    displayResult(solution, minimum)


def createProblem():
    fileName = input('Input file name :')
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


def firstChoice(p):
    current = randomInit(p)
    valueC = evaluate(current, p)

    i = 0
    while i < LIMIT_STUCK:
        successor= randomMutant(current, p)
        valueS = evaluate(successor, p)

        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0
        else:
            i += 1

    return current, valueC


def randomInit(p):
    numCities = p[0]
    init = list(range(numCities))
    random.shuffle(init)
    return init


def evaluate(current, p):
    global NumEval
    NumEval += 1

    cost = 0
    numCities = p[0]
    table = p[2]

    for i in range(numCities - 1):
        locFrom = current[i]
        locTo = current[i + 1]
        cost += table[locFrom][locTo]
    return cost


def randomMutant(current, p):
    while True:
        i, j = sorted([random.randrange(p[0]) for _ in range(2)])
        if i < j:
            curCopy = inversion(current, i, j)
            break
    return curCopy


def inversion(current, i, j):
    curCopy = current[:]
    while i < j:
        curCopy[i], curCopy[j] = current[j], current[i]
        i += 1
        j -= 1
    return curCopy


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
    print("Search algorithm: First-Choice Hill Climbing")

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
