'''
Find the second smallest number from the list/array
 ip = [89,90,87,65,44] O=65
ip = [23,45,67,32,10] O=23
'''
import heapq
def secondSmallest(arr):
    heap = []
    k = 2
    for i in arr:
        heapq.heappush(heap,-i)
        if len(heap) > k:
            heapq.heappop(heap)
            
    
    print(-1*heap[0])
    print('------------------')
    return -1 * heap[0]

ip = [89,90,87,65,44] 
ip2 = [23,45,67,32,10]
ans = secondSmallest(ip)
ans = secondSmallest(ip2)
        

        