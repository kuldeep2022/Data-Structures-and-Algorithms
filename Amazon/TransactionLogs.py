'''
Asked in Amazon OA 2021

Users that perform an excessive amount of transactions might be abusing the service so you have been tasked to identify the users that have a number of transactions over a threshold. The list of user ids should be ordered in ascending numeric value.
Example
threshold = 2
logs = ["88 99 200", "88 99 300", "99 32 100", " 12 12 15"]
output = ["88", "99"]
'''

#using Sorting
def processLog(logs, threshold):
    hashmap = {}
    for j in logs:
        a = j.split()
        for i in range(2):
            if a[i] == a[i + 1]:
                hashmap[a[i]] = hashmap.get(a[i], 0) + 1
                break
            else:
                hashmap[a[i]] = hashmap.get(a[i], 0) + 1
    res = [int(k) for k, v in hashmap.items() if v >= threshold]
    res.sort()
    print("Ans", [str(i) for i in res])

logs1 = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
logs2 = ["1 2 50","1 7 70", "1 3 20", "2 2 17"]
logs4 = ["345366 89921 45","029323 38239 23","38239 345366 15","029323 38239 77","345366 38239 23","029323 345366 13","38239 38239 23"]
logs3 = ["5 42 50"]

processLog(logs1,2)
processLog(logs2,2)
processLog(logs3,1)
processLog(logs4,3)


#using Heap
import heapq
def processLog2(logs, threshold):
    hashmap = {}
    for j in logs:
        a = j.split()
        for i in range(2):
            if i < 2 and a[i] == a[i + 1]:
                hashmap[a[i]] = hashmap.get(a[i], 0) + 1
                break
            else:
                hashmap[a[i]] = hashmap.get(a[i], 0) + 1
    heap = [int(k) for k, v in hashmap.items() if v >= threshold]
    heapq.heapify(heap)
    print("Ans", [str(heapq.heappop(heap)) for _ in range(len(heap))])

logs1 = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
logs2 = ["1 2 50","1 7 70", "1 3 20", "2 2 17"]
logs4 = ["345366 89921 45","029323 38239 23","38239 345366 15","029323 38239 77","345366 38239 23","029323 345366 13","38239 38239 23"]
logs3 = ["5 42 50"]

processLog2(logs1,2)
processLog2(logs2,2)
processLog2(logs3,1)
processLog2(logs4,3)