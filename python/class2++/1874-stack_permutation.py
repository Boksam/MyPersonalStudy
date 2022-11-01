from sys import stdin, stdout

N = int(stdin.readline())

my_list = [i for i in range(1, N + 1)]
stack = []
target_list = []
result = []

for _ in range(N):
    target_list.append(int(stdin.readline()))

for target in target_list:
    while not len(my_list) == 0 and my_list[0] <= target:
        result.append("+\n")
        stack.append(my_list.pop(0))
    
    if stack[-1] != target:
        result.clear()
        break
    else:
        result.append("-\n")
        stack.pop()

if len(result) != 0:
    for re in result:
        stdout.write(re)
else:
    stdout.write("NO\n")