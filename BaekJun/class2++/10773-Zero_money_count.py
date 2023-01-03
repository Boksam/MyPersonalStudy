from sys import stdin, stdout

stack = []

N = int(stdin.readline())

for _ in range(N):
    num = int(stdin.readline())
    
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

stdout.write(str(sum(stack)) + "\n")