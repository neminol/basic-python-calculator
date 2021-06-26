# Made by Quasm Systems for fun
# Basic calculator

num1 = input("Enter your number:")
num2 = input("Enter your number:")
operation = print("Enter your math operation (+ - * /)")
inputoperation = input()

plus = float(num1) + float(num2)
minus = float(num1) - float(num2)
multiply = float(num1) * float(num2)
divide = float(num1) / float(num2)

if inputoperation == "+":
    print(plus)

elif inputoperation == "-":
    print(minus)

elif inputoperation == "*":
    print(multiply)

elif inputoperation == "/":
    print(divide)

else:
    print("Cannot read operation.")
