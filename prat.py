num1 = float(input("enter 1 number:"))
num2 = float(input("enter 2 number:"))
num3 = float(input("enter 3 number:"))

smallest = 0
if (num1 <= num2) and (num1 <= num3):
  smallest =num1
elif (num2 <= num1) and (num2 <= num3):
  smallest = num3
else:
    smallest = num3
    print("the smalesr number is:",smallest)
