# 1

score = int(input('Enter your score: '))

if score >= 90:
    print('very good student')

elif score >= 80:
    print('good student')

elif score >= 70:
    print('normal student')

elif score >= 60:
    print('bad student')

else:
    print('very bad student')



# 2

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if num1 > num2:
    print('The first nuumber is greater than the second')

elif num1 < num2:
        print('The second number is greater than the first')

else:
     print('Both numbers are the same')



# 3

age = int(input('Enter age: '))

if age < 13:
     print('child')

elif age < 17:
     print('Teenager')

else:
     print('Adult')



# 4

budget = int(input('Enter your budget: '))

price = int(input('How much did you spend: '))

if price < budget:
     print(budget - price)

elif price == budget:
     print('You spent all your money')

else:
     print('Not enough money')