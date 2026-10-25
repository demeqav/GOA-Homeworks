# 1

numbers = [10, 20, 30, 40]

numbers.pop(1)

print(numbers)



# 2

fruits = ["apple", "banana", "orange", "kiwi"]

fruits.pop(-1)

print(fruits)



# 3

numbers = [1, 2, 4, 5]

numbers.insert(2, 3)

print(numbers)



# 4

names = ["Gio", "Nika", "Saba"]

names.append('luka')



# 5

colors = ["red", "blue", "green"]

colors.append('yellow')

print(colors)



# 6

numbers = [5, 10, 15]

numbers.append(20)

print(numbers)



# 7

numbers = [10, 20, 30, 40, 50]

numbers.pop(2)

numbers.append(100)

print(numbers)



# 8

fruits = ["apple", "banana", "orange"]

fruits.insert(1, 'kiwi')

fruits.append('mango')

print(fruits)



# 9

numbers = [1, 2, 3, 4]

numbers.extend([5, 6, 7])

numbers.pop(0)

print(numbers)



# 10

names = ["Gio", "Nika", "Saba", "Luka"]

names.remove('Nika')

names.insert(1, 'dato')

print(names)



# 11

numbers = [5, 10, 15, 20, 25]

numbers.remove(15)

numbers.extend([30, 35])

print(numbers)



# 12

colors = ["red", "blue", "green"]

colors.append('yellow')

colors.insert(1, 'black')

colors.pop(-1)



# 13

numbers = [15, 5, 30, 10, 20]

numbers.append(25)

numbers.insert(2, 100)

numbers.sort()



# 14

fruits = ["apple", "banana", "kiwi", "banana", "orange"]

banana_count = fruits.count('banana')

fruits.remove('banana')

print(fruits)

print(banana_count)



# 15

numbers = [10, 20, 30, 40, 50, 60]

numbers.pop(2)

numbers.insert(2, 25)

numbers.index(40)



# 16

numbers = [8, 3, 12, 5, 3, 9, 3]

count_numbers = numbers.count(3)

numbers.remove(3)

numbers.append(15)

print(numbers)

print(count_numbers)



# 17

numbers = [4, 9, 2, 7, 1, 6]

numbers.sort()

numbers.reverse()

print(numbers)



# 18

names = ["Gio", "Nika", "Saba", "Luka"]

saba_index = names.index('Saba')

names.insert(saba_index, "Dato")

print(names)



# 19

numbers = [10, 20, 30, 40, 50]

numbers.extend([60, 70, 80])

numbers.sort()

numbers.pop()

print(numbers)



# 20

fruits = ["apple", "orange", "apple", "kiwi", "banana", "apple"]

apple_count = fruits.count('apple')

kiwi_index = fruits.index('kiwi')

fruits.remove('apple')

fruits.reverse()

print(fruits)

print(apple_count)

print(kiwi_index)



# 21

numbers = [25, 10, 40, 15, 30, 10]

count_10 = numbers.count(10)

numbers.append(50)

numbers.insert(2, 100)

numbers.insert(2, 100)

numbers.sort()

numbers.pop(-1)

print(numbers)

print(count_10)