
def filter_func(c):
    filter_set = {"(", ")", "[", "]"}
    if c in filter_set:
        return True
    return False

while True:
    line = input()
    if line == ".":
        break
    brackets = list(filter(filter_func, line))
    
    count_small = 0
    count_large = 0
    is_balance = True

    for bracket in brackets:
        if bracket == "(":
            count_small += 1

        elif bracket == "[":
            count_large += 1

        elif bracket == ")":
            count_small -= 1
            if count_large % 2 != 0:
                is_balance = False
                break
        elif bracket == "]":
            count_large -= 1
            if count_small % 2 != 0:
                is_balance = False
                break
        
        if count_small < 0 or count_large < 0:
            is_balance = False
            break
        
    if count_small != 0 or count_large != 0:
        is_balance = False
   
    if is_balance:
        print("yes")
    else:
        print("no")
    

# ( [ ( ) ])
  1 2 1 1 0 0