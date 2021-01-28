if __name__ == '__main__':
    cmd = []                        #Stores the commands in a list
    arr = []                        #Stores list elements acc to commands
    N = int(input())                
    for _ in range(N):
        command = input().split()
        cmd.append(command)
        if command[0] == "insert":
            pos = int(command[1])   #Commands with more than one statements
            num = int(command[2])   #split with " "
            arr.insert(pos,num)
        elif command[0] == "remove":
            num = int(command[1])
            arr.remove(num)
        elif command[0] == "append":
            num = int(command[1])
            arr.append(num)
        elif command[0] == "sort":
            arr.sort()
        elif command[0] == "pop":
            arr.pop()
        elif command[0] == "reverse":
            arr.reverse()
        elif command[0] == "print":
            print(arr)