zero = {0 : 1, 1 : 0, 2 : 1}
one = {0 : 0, 1 : 1, 2 : 1}

def fibonacci(num):
    global zero, one

    if num in zero:
        return zero[num], one[num]
    else:
        for i in range(len(zero), num + 1):
            zero[i] = zero[i-1] + zero[i-2]
            one[i] = one[i-1] + one[i-2]
        return zero[num], one[num]



N = int(input())

for _ in range(N):
    num = int(input())
    zero_count, one_count = fibonacci(num)
    print(zero_count, one_count)