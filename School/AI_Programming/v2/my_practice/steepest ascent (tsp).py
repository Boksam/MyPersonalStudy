from problem import Tsp


def main():
    p = Tsp()

    p.setVariables()

    steepestAscent(p)

    p.describe()
    displaySetting(p)
    p.report()


def steepestAscent(p):
    current = p.randomInit()
    valueC = p.evaluate(current)

    while True:
        neighbors = p.mutants(current)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    p.storeResult(current, valueC)


def bestOf(neighbors, p):
    best = neighbors[0]
    bestValue = p.evaluate(best)

    for i in range(1, len(neighbors)):
        newValue = p.evaluate(neighbors[i])
        
        if newValue < bestValue:
            bestValue = newValue
            best = neighbors[i]
    return best, bestValue


def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")


main()
