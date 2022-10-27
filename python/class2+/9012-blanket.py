N = int(input())

for i in range(N):
    str_list = input()
    result = 0
    for c in str_list:
        if result < 0:
            break

        if c == "(":
            result += 1
        elif c == ")":
            result -= 1
    
    if result == 0:
        print("YES")
    else:
        print("NO")