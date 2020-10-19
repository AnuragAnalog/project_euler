
primes = [2,3]
FactorsData = [[0],{1:1},{1:1,2:1},{1:1,3:1}]
nList = [0,1,2,2]
import time

def mergeDicts(baseDict,addendDict):
    retDict = addendDict.copy()
    for key,value in baseDict.items():
        if key not in retDict.keys():
            retDict.setdefault(key,value)
        else:
            retDict[key] += value
    return retDict

def n(i):
    prime = True
    fDict = {}
    for j in primes:
        if i%j == 0:
            prime = False
            k = int(i/j)
            fDict.setdefault(j,1)
            kFactors = FactorsData[k]
            prevCount = kFactors.get(j,0) + 1
            fDict = mergeDicts(fDict,kFactors)
            newCount = fDict[j]  + 1
            nFactors = int((nList[k]*newCount)/prevCount)
            nList.append(nFactors)
            break
    if prime == True:
        primes.append(i)
        fDict = {1:1,i:1}
        nList.append(2)
    FactorsData.append(fDict)

num = 3
start = time.time()

def CheckResult(halfValue,num2,n1,n2):
    if n1 * n2 >= 500 :
        k = halfValue * num2
        print(f" answer: {k}")
        return True
    else:
        return False

while True :
    nxtNum = num + 1
    n(nxtNum)
    if num %2 == 0:
        half = int(num/2)
        n1 = nList[half]
        n2 = nList[nxtNum]
        breakVal = CheckResult(half,nxtNum,n1,n2)
        if breakVal == True:
            break
    else:
        half = int(nxtNum/2)
        n1 = nList[num]
        n2 = nList[half]
        breakVal = CheckResult(half,num,n1,n2)
        if breakVal == True:
            break
    num += 1
        
end = time.time()
print(f" execution time:  {end - start}seconds")
