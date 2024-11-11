# Write a program to check if a number is present in the list or not. If the number is present, print the position of the number.Print an appropriate message if the number is not present in the list.
list1 = []
print("How many numbers do you want to enter in the list: ")
maximum = int(input())
print("Enter a list of numbers:")
for i in range(0,maximum):
    n = int(input())
    list1.append(n)
num = int(input("Enter the number to be searched: "))
 
position = -1
for i in range (0, lin (list1)):
if list1[i] == num:
    position = i+1
    if position == -1:
        print("Numbber",num,"is not present in the list")
    else:
        print("Number",num,"is present at",position+1,"position")
