def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

arr = [3,5,1,6,9,4,8] 
  
bubbleSort(arr) 
  
print ("Array ordenado:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]),  
