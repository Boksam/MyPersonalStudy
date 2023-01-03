import random
import math

DELTA = 0.01
LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement
NumEval = 0


def main():
    p = createProblem()

    solution, minimum = firstChoice(p)

    describeProblem(p)
    displaySetting()
    displayResult(solution, minimum)


def createProblem():
    fileName = input("Input file name :")
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
    infile.close()

    domain = [varNames, low, up]

    return expression, domain


def firstChoice(p):
    current = randomInit(p)
    valueC = evaluate(current, p)

    i = 0
    while i < LIMIT_STUCK:
        successor = randomMutant(current, p)
        valueS = evaluate(successor, p)

        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0
        else:
            i += 1

    return current, valueC


def randomInit(p):
    domain = p[1]
    low, up = domain[1], domain[2]
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


def randomMutant(current, p):
    i = random.randint(0, len(current) - 1)
    if random.uniform(0, 1) > 0.5:
        d = DELTA
    else:
        d = -DELTA
    return mutate(current, i, d, p)


def mutate(current, i, d, p):
    curCopy = current[:]
    domain = p[1]
    l = domain[1][i]
    u = domain[2][i]

    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy


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
    print("Search algorithm: First-Choice Hill Climbing")
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
