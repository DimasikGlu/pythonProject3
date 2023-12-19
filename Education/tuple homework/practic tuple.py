# Task1
'Написать программу для конвертации кортежа в string'
tup1 = (3.4, 56, "Some", "Hi", 7, 3.8, 44)
str = str(tup1)
print(type(str))

# Task2
'Написать программу, которая находит длину кортежа'
print(len(tup1))

# Task3
print(tup1[-3])
print(tup1[2::2])

# Task4
'convert to tuple'
numList = [213,43,5,6,86]
numlisttup = tuple(numList)
print(type(numlisttup))

# Task 5
'create tuple and print'
tuple2 = (5,7,'name', 'city',5.3,7.2)
i = 0
while i <= len(tuple2):
    i +=1
    a = tuple2[i]
    print(a)
