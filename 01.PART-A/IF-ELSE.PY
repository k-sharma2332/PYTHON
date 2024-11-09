# IF CONDITION
age = int(input("enter the age"))
if age>18:
    print("adult")

# IF-ELSE CONDITION
num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))
if num1 > num2:
    diff = num1-num2
else:
    diff = num2-num1
    print(diff)

# IF-ELSEIF-ELSE
num1 = int(input("Enter the number "))
if num1>0:
    print("num1 is positive")
elif num1<0:
    print("num1 is negative")
else:
    print("num1 is zero")