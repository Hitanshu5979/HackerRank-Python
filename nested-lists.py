if __name__ == '__main__':
    namelist = []           #Stores student names in a list
    scorelist = []          #Stores student scores in a list
    low2names = []          #Stores student names with second lowest score

    for _ in range(int(input())):
        name = input()
        score = float(input())
        namelist.append(name)
        scorelist.append(score)
    
    low = min(scorelist)                            #Stores lowest score
    while min(scorelist) == low:
        lowindex = scorelist.index(min(scorelist))  #Stores index of lowest score
        scorelist.remove(min(scorelist))            #Removes lowest score from scorelist
        del namelist[lowindex]                      #Deletes the student name with lowest marks

    low2 = min(scorelist)                                               #Stores second lowest score

    while min(scorelist) == low2:
        low2names.append(namelist[scorelist.index(min(scorelist))])     #Stores student names with second lowest scores
        low2index = scorelist.index(min(scorelist))                     #Stores index of second lowest score
        scorelist.remove(min(scorelist))                                #Removes second lowest score from scorelist
        del namelist[low2index]                                         #Deletes the student name with second lowest marks
        if len(scorelist) == 0:                                         #Checks if scorelist is empty
            break

    low2names.sort()            #Sorts student names with second lowest marks in alphabetical manner
    for nm in low2names:
        print(nm)