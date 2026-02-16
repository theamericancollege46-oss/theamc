num = int(input("Enter the number:"))

if num < 0:
    num = int(input("please enter the postive number")) 
sum = 0
while num > 0:
    sum += num
    num -=1
    print("The natural number is:",sum)
