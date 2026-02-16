num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
num3 = float(input("Enter the third number:"))

greatest = num1
if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
print(F"The greatest number is :{greatest}")
