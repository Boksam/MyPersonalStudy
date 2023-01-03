tree_num, target_len = map(int, input().split())

tree_list = list(map(int, input().split()))

start, end = 1, max(tree_list)

while start <= end:
    mid = (start + end) // 2
    cutted = 0
    
    for tree in tree_list:
        if tree > mid:
            cutted += tree - mid

    if cutted >= target_len:
        start = mid + 1
    else:
        end = mid - 1

print(end)