import heapq
H=[2,3,7,9,8]
heapq.heapify(H)
print( "HEAP: ",H)
#Insertion
heapq.heapify(H)
heapq.heappush(H,69)
print("Modified Heap: ",H)
#Removal
heapq.heapify(H)
heapq.heappop(H)
print("popped heap: ",H)
#Replace
heapq.heapify(H)
heapq.heapreplace(H,6)
print("replace heap: ",H)




