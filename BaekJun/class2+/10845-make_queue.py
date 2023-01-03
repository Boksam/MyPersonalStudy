from sys import stdin, stdout

num_queue = []

N = int(stdin.readline())
for i in range(N):
    query = stdin.readline().split()
    if query[0] == "push":
        num_queue.append(query[1])
    elif query[0] == "pop":
        if len(num_queue) == 0:
            stdout.write("-1\n")
        else:
            stdout.write(num_queue.pop(0) + "\n")
    elif query[0] == "size":
        stdout.write(str(len(num_queue)) + "\n")
    elif query[0] == "empty":
        if len(num_queue) == 0:
            stdout.write("1\n")
        else:
            stdout.write("0\n")
    elif query[0] == "front":
        if len(num_queue) == 0:
            stdout.write("-1\n")
        else:
            stdout.write(num_queue[0] + "\n")
    elif query[0] == "back":
        if len(num_queue) == 0:
            stdout.write("-1\n")
        else:
            stdout.write(num_queue[-1] + '\n')
    