import math

operator = input("Enter an operator (+,-,:,x)")
num1 = float(input("Enter  the first number "))
num2 = float(input("Enter the second number "))


if operator == "+":
    print(num1 + num2)
if operator == ":":
    print(num1 / num2)
if operator == "-":
    print(num1 - num2)
if operator == "x":
    print(num1 * num2)
