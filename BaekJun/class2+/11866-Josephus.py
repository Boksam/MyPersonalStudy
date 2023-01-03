from sys import stdin, stdout

N, K = map(int, stdin.readline().split())

circle_list = [i for i in range(1, N + 1)]

idx = 0
stdout.write("<")

while True:
    if len(circle_list) == 1:
        break
    idx += K - 1
    if idx >= len(circle_list):
        idx %= len(circle_list)
    
    stdout.write(str(circle_list[idx]) + ", ")
    del circle_list[idx]

stdout.write(str(circle_list[0]) + ">\n")
