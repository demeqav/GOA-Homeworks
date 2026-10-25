# 3

number = int(input('Enter number: '))

if number > 0:
    if number > 10:
        print("Greater than 10")
    else:
        print("10 or less")
else:
    print("Negative or zero")


# 4

age = int(input("Enter age: "))

if age >= 18:
    if age < 65:
        print("Between 18 and 64")
    else:
        print("65 or older")
else:
    print("Minor")


# 5

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if num1 > num2:
    if num1 > 100:
        print("The first number is greater than 100")
    else:
        print("The first number is not greater than 100")
else:
    print("The first number is not greater")


# 6

number1 = int(input())

if number1 % 2 == 0:
    if number1 > 20:
        print("Even number greater than 20")
    else:
        print("Even number is not greater than 20")
else:
    print("Odd number")


# 7

temperature = int(input())

if temperature > 20:
    if temperature > 30:
        print("Greater than 30")
    else:
        print("Between 21 and 30")
else:
    print("Cold")


# 8

score = int(input())

if score >= 50:
    if score > 90:
        print("Greater than 90")
    else:
        print("Passed")
else:
    print("You failed the exam")


# 9

price = float(input('Enter price: '))
money = float(input('Enter money: '))

if money >= price:
    if money == price:
        print("You have exactly enough money")
    else:
        print("You have more money than needed")
else:
    print("You don't have enough money")


# 10

number3 = int(input('Enter number: '))

if number3 > 0:
    if number3 > 50:
        print("Greater than 50")
    else:
        print("50 or less")
else:
    print("The number is not positive")


# 11

num4 = int(input('Enter first: '))
num5 = int(input('Enter second number: '))

if num4 == num5:
    print("Equal")
else:
    if num4 > num5:
        print("The first number is greater")
    else:
        print("The second number is greater")


# 12

age = int(input('Enter age: '))

if age >= 18:
    if age >= 21:
        print("21 or older")
    else:
        print("Between 18 and 20")
else:
    print("Under 18")