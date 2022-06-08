import heapq


arr =[-74, 0, -4, 20, 7, 1, -4700, 74, 21, 71000, 87, 400, 9]
print ("The array: ", arr)
print("")
heapArray = arr
length = len(arr)
heapq.heapify(heapArray)
sortedArray = []

for each in (arr[:length]):
    sortedArray.append(heapq.heappop(heapArray))
    
arr = sortedArray
print ("The sorted array is:", arr)
