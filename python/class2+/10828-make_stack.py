from sys import stdin

N = int(stdin.readline())

my_stack = []

for i in range(N):
    query_num = stdin.readline().split()
    if query_num[0] == "push":
        my_stack.append(query_num[1])
    elif query_num[0] == "pop":
        if len(my_stack) == 0:
            print("-1")
        else:
            print(my_stack.pop())
    elif query_num[0] == "size":
        print(len(my_stack))
    elif query_num[0] == "empty":
        if len(my_stack) == 0:
            print("1")
        else:
            print("0")
    elif query_num[0] == "top":
        if len(my_stack) == 0:
            print("-1")
        else:
            print(my_stack[-1])