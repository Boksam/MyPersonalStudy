
def filter_func(c):
    filter_set = {"(", ")", "[", "]"}
    if c in filter_set:
        return True
    return False

def solve(i):
    end_str = ""
    if brackets[i] == "(":
        end_str = ")"
    else:
        end_str = "]"
    
    sum1 = 0
    sum2 = 0
    i += 1
    while i < len(brackets):
        if brackets[i] == end_str:
            if sum1 == 0 and sum2 == 0:
                return True, i
            else:
                return False, i
        
        if brackets[i] == "(":
            sum1 += 1
        elif brackets[i] == "[":
            sum2 += 1
        elif brackets[i] == ")":
            sum1 -= 1
        else:
            sum2 -= 1
        i += 1
    
    if sum1 != 0 or sum2 != 0:
        return False, i
    return True, i
        
        
    

while True:
    line = input()
    if line == ".":
        break
    brackets = list(filter(filter_func, line))
    
    result = False
    idx = 0
    while idx < len(brackets):
        if brackets[idx] == "(" or brackets[idx] == "[":
            result, idx = solve(idx)
            if result == False:
                break
        else:
            result = False
            break
        idx += 1
    
    if result == True:
        print("yes")
    else:
        print("no")
    
        
    

    # So when I die (the [first] I will see in (heaven) is a score list).
    # [ first in ] ( first out ).
    # Half Moon tonight (At least it is better than no Moon at all].
    # A rope may form )( a trail in a maze.
    # Help( I[m being held prisoner in a fortune cookie factory)].
    # ([ (([( [ ] ) ( ) (( ))] )) ]).