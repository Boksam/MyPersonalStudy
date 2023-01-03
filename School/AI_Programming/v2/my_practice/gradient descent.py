from problem import Numeric


def main():
    p = Numeric()
    
    p.setVariables()

    gradientDescent(p)

    p.describe()
    displaySetting(p)
    p.report()


def gradientDescent(p):
    currentP = p.randomInit()
    valueC = p.evaluate(currentP)

    while True:
        nextP = p.takeStep(currentP, valueC)
        valueN = p.evaluate(nextP)
        if valueN >= valueC:
            break
        else:
            currentP = nextP
            valueC = valueN
    p.storeResult(currentP, valueC)


def displaySetting(p):
    print()
    print("Search algorithm: Gradient Descent")
    print()
    print("Update rate:", p.getAlpha())
    print("Increment for calculating derivative:", p.getDx())


main()
