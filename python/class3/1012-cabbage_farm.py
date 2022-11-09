import sys
sys.setrecursionlimit(10000)

farm= []
visited = []
count = 0

def DFS(start_point):
    global farm, count

    current_point = start_point
    farm.remove(start_point)

    for block in farm:
        if abs(block[0] - current_point[0]) + abs(block[1] - current_point[1]) == 1:
            DFS(block)


n = int(sys.stdin.readline())
for _ in range(n):
    farm = []
    visited = []
    count = 0

    M, N, K = map(int, sys.stdin.readline().split())
    
    for __ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        farm.append((x, y))
    while farm:
        DFS(farm[0])
        count += 1
    
    sys.stdout.write(str(count) + '\n')