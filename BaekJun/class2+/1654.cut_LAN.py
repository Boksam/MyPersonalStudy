N, K = map(int, input().split())

lan_list = []

max_lan_len = 0
for _ in range(N):
    lan_list.append(int(input()))
    if max_lan_len < lan_list[-1]:
        max_lan_len = lan_list[-1]

start, end, mid = 1, max_lan_len, 0
while start <= end:
    mid = (start + end) // 2
    result = 0
    for lan in lan_list:
        result += lan // mid

    if result >= K:
        start = mid + 1
    else:
        end = mid - 1
print(end)