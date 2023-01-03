
def filter_bracket(c):
    brackets_set = {"(", ")", "[", "]"}
    if c in brackets_set:
        return True
    else:
        return False

while True:
    stack = []
    brackets = []

    line = input()
    if line == ".":
        break

    for c in line:
        if filter_bracket(c):
            brackets.append(c)
    
    if len(brackets) == 0:
        print("yes")
        continue
    
    result = True
    for bracket in brackets:
        if bracket == "(" or bracket == "[":
            stack.append(bracket)
        elif bracket == ")":
            if len(stack) == 0 or stack[-1] != "(":
                result = False
                break
            else:
                stack.pop()
        elif bracket == "]":
            if len(stack) == 0 or stack[-1] != "[":
                result = False
                break
            else:
                stack.pop()
    
    if result and len(stack) == 0:
        print("yes")
    else:
        print("no")