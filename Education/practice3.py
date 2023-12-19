# 1 Task
import copy

num = [123, 4, 45, 6, 7]
print(f"{max(num)}")
# 2 Task
numList = [21, 43, 54, 6, 76, 8, 34]
# sum
SumnumList = sum(numList)
print(f"{SumnumList}")
# avg
avgnumlist = (SumnumList / len(numList))
print(f"{avgnumlist}")
# 3 Task
alphabetList = ['a', 's', 'd', 't']
# sorted (reversed) alphavite
print(sorted(alphabetList))
print(sorted(alphabetList, reverse=True))
# 4 Task
# add 45, 61 in task 1
# num2 = (num) + [45, 61] #способ 2
num.insert(5, 45)
num.insert(6, 61)
# print(f"{num2}")
print(f"{num}")
# delete 2 elements
print(len(numList))
num3 = numList[0:5]
# item = [8, 34] - 2 sposob
# if item in numList:
#     numList.remove(item)
print(f"{num3}")
# 5 Task
someList = [12, 454, 65, 76, 1, 23]
someList2 = someList
print (someList)
print (someList2)
# deep copy
someList2 = copy.deepcopy(someList)
print (someList)
print (someList2)