import random
import math

DELTA = 0.01
NumEval = 0

def main():
    p = createProblem()

    solution, minimum = steepestAscent(p)

    describeProblem(p)
    displaySetting()
    displayResult(solution, minimum)

def createProblem():
    fileName = input("Enter file name :")
    infile = open(fileName, 'r')
    
    expression = infile.readline()
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
    domain = [varNames, low, up]
    
    return expression, domain
    

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
    domain = p[1]
    low = domain[1]
    up = domain[2]

    init = []
    for i in range(len(low)):
        r = random.uniform(low[i], up[i])
        init.append(r)
    return init

def evaluate(current, p):
    global NumEval
    NumEval += 1

    expr = p[0]
    varNames = p[1][0]

    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment)
    return eval(expr)


def mutants(current, p):    # return neighbors
    neighbors = []

    for i in range(len(current)):
        mutant = mutate(current, i, DELTA, p)
        neighbors.append(mutant)
        mutant = mutate(current, i, -DELTA, p)
        neighbors.append(mutant)

    return neighbors

def mutate(current, i, d, p):
    curCopy = current[:]
    low, up = p[1][1][i], p[1][2][i]

    if low <= (curCopy[i] + d) <= up:
        curCopy[i] += d
    return curCopy


def bestOf(neighbors, p):
    best = neighbors[0]
    bestValue = evaluate(best, p)

    for i in range(1, len(neighbors)):
        newValue = evaluate(neighbors[i], p)
        if newValue < bestValue:
            bestValue = newValue
            best = neighbors[i]
    return best, bestValue

def describeProblem(p):
    print()
    print("Objective function:")
    print(p[0])   # Expression
    print("Search space:")
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 

def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple


main()