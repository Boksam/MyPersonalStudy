N = int(input())
a = set(input().split())

M = int(input())
b = input().split()

for num in b:
    if num in a:
        print("1")
    else:
        print("0")