from sys import stdin, stdout

blocks = []
N, M, B = map(int, stdin.readline().split())

def time_calc(num):
    time = 0
    inventory = B

    for block in blocks:
        diff = block - num
        if diff > 0:
            time += 2 * diff
            inventory += diff
        else:
            time += abs(diff)
            inventory -= abs(diff)
    
    if inventory < 0:
        return False, time
    else:
        return True, time




for _ in range(N):
    blocks.extend(list(map(int, stdin.readline().split())))

min_time = -1
max_height = max(blocks)
for height in range(min(blocks), max(blocks) + 1):
    possible, time = time_calc(height)
    
    if possible:
        if min_time == -1:
            min_time = time
            max_height = height
        elif min_time == time:
            max_height = max(max_height, height)
        elif min_time > time:
            min_time = time
            max_height = height

print(min_time, max_height)