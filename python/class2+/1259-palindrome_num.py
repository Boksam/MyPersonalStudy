while (True):
    num_list = list(input())
    if num_list == ["0"]:
        break
    
    if num_list == list(reversed(num_list)):
        print("yes")
    else:
        print("no")