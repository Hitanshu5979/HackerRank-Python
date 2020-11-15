if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    #Converting Mapped Objects into List
    scores = list(arr)  #Done in order to use list operations
    
    high = max(scores)
    
    while (high == max(scores)):
        scores.remove(max(scores))  #Removes the highest score and it's duplicate entries
    
    print(max(scores))  #Prints Runner-Up Score
