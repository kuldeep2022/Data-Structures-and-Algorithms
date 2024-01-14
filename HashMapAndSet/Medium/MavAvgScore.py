def maxAvgSum(arr):
    d = {}
    for i in range(len(arr)):
        if arr[i][0] not in d:
            d[arr[i][0]] = []
        d[arr[i][0]].append(arr[i][1])
    # print(d)
    maxAvg = 0
    person = ""
    for k,v in d.items():
        calc = sum(v)//len(v)
        # print("Person",k,'Max Avg Score',calc)
        if calc > maxAvg:
            maxAvg = calc
            person = k
    
    # print(person)
    return person
            
            

arr = array=[['Ann',45,],['king',35],['abel',44],['king',10],['king',70],['Ann',51],['Ann',10]]
ans = maxAvgSum(arr)