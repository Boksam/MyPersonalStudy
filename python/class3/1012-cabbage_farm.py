from sys import stdin, stdout

farm= []
visited = []
count = 0

def DFS(start_point):
    global farm, count
    farm.pop()

    for block in farm:
        if block not in visited and abs(block[0] - start_point[0]) + abs(block[1] - start_point[1]) == 1:
            DFS(block)


n = int(stdin.readline())
for _ in range(n):
    farm = []
    visited = []
    count = 0

    M, N, K = map(int, stdin.readline().split())
    
    for __ in range(K):
        x, y = map(int, stdin.readline().split())
        farm.append((x, y))
    while farm != visited:
        DFS(farm[0])
        count += 1
    
    stdout.write(str(count) + '\n')