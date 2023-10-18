# insertion Sort
def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        #    
        arr[j + 1] = key 
# list 
a = [40 , 60 , 35, 99 ,100 ,1, 34,]

print("befor : " , a)
insertionSort(a)
print("after : ",  a)

# befor :  [40, 60, 35, 99, 100, 1, 34]
# after :  [1, 34, 35, 40, 60, 99, 100]