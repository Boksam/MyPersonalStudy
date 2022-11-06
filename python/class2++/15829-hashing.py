sum = 0
R = 31
M = 1234567891

N = int(input())
my_str = input()

for i in range(N):
    str_to_num = ord(my_str[i]) - ord('a') + 1
    sum += str_to_num * (R ** i)

sum %= M
print(sum)