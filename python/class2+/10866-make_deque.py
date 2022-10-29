from sys import stdin, stdout

num_deque = []

N = int(stdin.readline())
for i in range(N):
    query = stdin.readline().split()
    if query[0] == "push_front":
        num_deque.insert(0, query[1])
    elif query[0] == "push_back":
        num_deque.append(query[1])
    elif query[0] == "pop_front":
        if len(num_deque) == 0:
            stdout.write("-1\n")
        else:
            stdout.write(num_deque.pop(0) + '\n')
    elif query[0] == "pop_back":
        if len(num_deque) == 0:
            stdout.write("-1\n")
        else:
            stdout.write(num_deque.pop() + '\n')
    elif query[0] == "size":
        stdout.write(str(len(num_deque)) + '\n')
    elif query[0] == "empty":
        if len(num_deque) == 0:
            stdout.write("1\n")
        else:
            stdout.write("0\n")
    elif query[0] == "front":
        if len(num_deque) == 0:
            stdout.write("-1\n")
        else:
            stdout.write(num_deque[0] + '\n')
    elif query[0] == "back":
        if len(num_deque) == 0:
            stdout.write("-1\n")
        else:
            stdout.write(num_deque[-1] + '\n')