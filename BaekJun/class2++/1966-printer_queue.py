from gettext import find


N = int(input())

for _ in range(N):
    list_size, target_idx = map(int, input().split())
    count = 1

    num_list = list(map(int, input().split()))
    
    while True:
        if num_list[0] == max(num_list):
            if target_idx == 0:
                print(count)
                break
            else:
                num_list.pop(0)
                count += 1
                target_idx -= 1
        else:
            if target_idx == 0:
                num_list.append(num_list.pop(0))
                target_idx = len(num_list) - 1
            else:
                num_list.append(num_list.pop(0))
                target_idx -= 1