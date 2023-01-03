from problem import Numeric


def main():
    p = Numeric()

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

        if valueC <= valueS:
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
            best = neighbors[i]
            bestValue = newValue
    return best, bestValue


def displaySetting(p):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta())

main()
