def swap_case(s):
    swapstring = ""                         #Stores String after case swapping
    for letter in s:
        if letter.isupper():
            swapstring += (letter.lower())  #Converts uppercase letter to lowercase
        elif letter.islower():
            swapstring += (letter.upper())  #Converts lowercase letter to uppercase
        elif letter.isspace:
            swapstring += letter
    return swapstring

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)