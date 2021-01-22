if __name__ == '__main__':
    n = int(input())                        #Stores no. of records to be taken
    student_marks = {}                      #Dictionary to store name:[marks]
    tot = 0
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))     #List to store scores of a student
        student_marks[name] = scores        #Dictionary stores value = [scores] with key = name
    query_name = input()                    #Student who's avg is to be calculated

    for name in student_marks:                          #Iterates through the dictionary
        if query_name == name:                          #Checks for query_name in dictionary
            for query_marks in student_marks[name]:     #Iterates through scores of query_name
                tot += query_marks                      
            avg = tot/3
            print("{:.2f}".format(avg))                 #Formats the answers to 2 decimal points