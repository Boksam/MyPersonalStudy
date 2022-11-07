from sys import stdin, stdout

farm = []
count = 0
def DFS():
    global farm, count
    
    for block in farm:
        
    
    



N = int(stdin.readline())
for _ in range(N):
    farm = []
    count = 0

    M, N, K = map(int, stdin.readline().split())
    
    for __ in range(K):
        x, y = map(int, stdin.readline().split())
        farm.append((x, y))
    
    DFS()
    
    stdout.write(str(count) + '\n')