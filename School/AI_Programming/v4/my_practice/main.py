from problem import *
from optimizer import *


def main():
    p, alg = readPlanAndCreate()
    conductExperiment(p, alg)
    p.describe()
    alg.displayNumExp()
    alg.displaySetting()
    p.report()


def readPlanAndCreate():
    parameters = readValidPlan()
    p = createProblem(parameters)
    alg = createOptimizer(parameters)
    return p, alg


def readValidPlan():
    while True:
        parameters = readPlan()
        if parameters['pType'] == 2 and parameters['aType'] == 4:
            print("You cannot choose Gradient Descent")
            print("       unless your want a numerical optimization.")
        else:
            break
    return parameters


def readPlan():
    fileName = input("Enter the file name:")
    infile = open(fileName, 'r')
    parameters = { 'pType':0, 'pFileName':'', 'aType':0, 'delta':0,
                   'limitStuck':0, 'alpha':0, 'dx':0, 'numRestart':0,
                   'limitEval':0, 'numExp':0 }
    parNames = list(parameters.keys())
    for i in range(len(parNames)):
        line = lineAfterComments(infile)
        if parNames[i] == 'pFileName':
            parameters[parNames[i]] = line.rstrip().split(':')[-1][1:]
        else:
            parameters[parNames[i]] = eval(line.rstrip().split(':')[-1][1:])
    infile.close()
    return parameters


def lineAfterComments(infile):
    line = infile.readline()
    while line[0] == '#':
        line = infile.readline()
    return line


def createProblem(parameters):
    pType = parameters['pType']
    if pType == 1:
        p = Numeric()
    elif pType == 2:
        p = Tsp()
    p.setVariables(parameters)
    return p


def createOptimizer(parameters):
    optimizers = { 1: 'SteepestAscent()',
                   2: 'FirstChoice()',
                   3: 'Stochastic()',
                   4: 'GradientDescent()',
                   5: 'SimulatedAnnealing()' }
    aType = parameters['aType']
    alg = eval(optimizers[aType])
    alg.setVariables(parameters)
    return alg


def conductExperiment(p, alg):
    aType = alg.getType()
    if 1 <= aType <= 4:
        alg.randomRestart(p)
    else:
        alg.run(p)
    bestSolution = p.getSolution()
    bestMinimum = p.getValue()
    numEval = p.getNumEval()
    
    sumOfMinimum = bestMinimum
    sumOfNumEval = numEval
    sumOfWhen = 0

    if 5 <= aType <= 6:
        sumOfWhen = alg.getWhenBestFound()
    numExp = alg.getNumExp()
    for i in range(1, numExp):
        if 1 <= aType <= 4:
            alg.randomRestart(p)
        else:
            alg.run(p)
        newSolution = p.getSolution()
        newMinimum = p.getValue()
        numEval = p.getNumEval()
        sumOfMinimum += newMinimum
        sumOfNumEval += numEval
        if 5 <= aType <= 6:
            sumOfWhen += alg.getWhenBestFound()
        if newMinimum < bestMinimum:
            bestSolution = newSolution
            bestMinimum = newMinimum
    avgMinimum = sumOfMinimum / numExp
    avgNumEval = round(sumOfNumEval / numExp)
    avgWhen = round(sumOfWhen / numExp)
    results = (bestSolution, bestMinimum, avgMinimum,
               avgNumEval, sumOfNumEval, avgWhen)
    p.storeExpResult(results)


main()