#Import
import math

#Input
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

#Sum of two number
sum = num1 + num2

#Xau du lieu

## Xau hoa du lieu
print("The first number is " + str(num1) + " and the second number is " + str(num2))

## Formated sentences
print(f"The first number is {num1} and the second number is {num2}")

## Format and brackets
text = "The first number is {0} and the second number is {1}"
print(text.format(num1,num2))

#Output
print(f"The sum of those two numbers is: {sum}")