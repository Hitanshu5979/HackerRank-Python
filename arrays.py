import numpy

def arrays(arr):
    a = numpy.array(arr,float)      #Stores values in a numpy array as float
    return a[::-1]                  #Returns reversed numpy array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)