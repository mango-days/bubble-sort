array = [1, 4, 9, 3, 5, 2, 8, 6, 7]
def bubbleSort (array):
    for i in range (0, len(array)-1):
        for j in range (0, len(array)-1-i):
            if array[j]>array[j+1]:
                temp=array[j+1]
                array[j+1]=array[j]
                array[j]=temp
    print(array)
bubbleSort (array)