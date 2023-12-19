# Task 1
x = 13
while x >= 1:
    print(x)
    x = x - 1
# Task 2
list = range(1,21)
x = int(0)
while x != sum(list[1:21:2]):
    x += 1
print(x)

# Task 3
list1 = range(15, 30)
x = float(0)
y = sum(list1) / len(list1)
while x != y:
    x += 1
print(x)

# Task 4
x = 34
while x<68:
    x += 1
    if x%2 == 0:
        print(x)