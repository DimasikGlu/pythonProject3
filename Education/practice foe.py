# Task 1
fruitlist = ['apple', 'banana', 'orange', 'pineapple', 'cherry']
num = 0
for i in fruitlist:
    print(i.title())
    num +=1
# Task 2
fruitlist2 = ['apple', 'banana', 'orange', 'pineapple', 'cherry']
num2 = 0
for i2 in fruitlist2:
    print(i2.upper())
    num2 +=1
# Task3
number = 0
num34 = 34
for i in range(5,58):
    number = i+number
    if i == num34:
        number -=34
    elif i == 46:
        number -=46
    elif i == 52:
        number -=52
print(number)

# Task 4
word_input = input("Введите слово:").lower()
num_input = int(input("Введите число повторений:"))
num = 0
for i in range(len(word_input)):
    word_input2 = word_input[i]
    print((word_input2)*(num_input))