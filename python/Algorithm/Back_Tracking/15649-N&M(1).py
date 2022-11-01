from sys import stdin, stdout

num_list = []
bool_num_list = []

def solve(m):
    global num_list, bool_num_list
    if m == M:
        for num in num_list:
            stdout.write(str(num) + " ")
        stdout.write('\n')
        return

    for num in range(1, N + 1):
        if bool_num_list[num - 1] == False:
            num_list.append(num)
            bool_num_list[num - 1] = True
            solve(m + 1)
            bool_num_list[num_list.pop() - 1] = False
            

if __name__ == "__main__":
    N, M = map(int, stdin.readline().split())
    bool_num_list = [False] * N
    solve(0)
