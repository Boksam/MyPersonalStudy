from problem import *
from optimizer import *

def main():
    # Select and create a Problem object
    p, pType = selectProblem()  # A specific problem and its type
    # Determine the search algorithm to be used
    alg = selectAlgorithm(pType)
    # Call the search algorithm
    alg.run(p)
    # Show the problem solved
    p.describe()
    # Show the algorithm settings
    alg.displaySetting()
    # Report results
    p.report()

def selectProblem():
    print("Select the problem type:")
    print("  1. Numerical Optimization")
    print("  2. TSP")
    pType = int(input("Enter the number: "))
    ###
    # Your code goes here!
    # 1. 클래스 생성
    # 2. 파일로 부터 문제 읽어오기
    if pType == 1:
        p = Numeric()
    elif pType == 2:
        p = Tsp()
    p.setVariables()
	
    return p, pType

def selectAlgorithm(pType):
    print()
    print("Select the search algorithm:")
    print("  1. Steepest-Ascent")
    print("  2. First-Choice")
    print("  3. Gradient Descent")
    ###
    # Your code goes here!
    # 1. 알고리즘 선택(단, invalid 함수를 사용해서 유효한 알고리즘이 선택될 때 까지 반복)
    # 2. 알고리즘에 해당하는 클래스 생성
    # 3. 생성한 알고리즘 클래스에 setVariables 호출하여 pType 저장
    while True:
        aType = int(input("Enter number:"))
        if not invalid(pType, aType):
            break
    optimizers = { 1: 'SteepestAscent()',
                   2: 'FirstChoice()',
                   3: 'GradientDescent()'}
    alg = eval(optimizers[aType])
    alg.setVariables(pType)
    return alg

def invalid(pType, aType):
    ###
    if pType == 2 and aType == 3:  # TSP 문제에서는 Gradient Descent 알고리즘 선택 불가
        print("You cannot choose Gradient Descent")
        print("   unless your want a function optimization.")
        return True
    else:
        return False


main()
