# A program to calculate average marks of n student where n is entered by the user.
list1 = []
n = int(input("Enter the element"))
for i in range (0,n):
    print("Enter marks of student",(i+1),":")
    marks = int(input())
    list1.append(marks)
    total = 0
    for marks in list1:
        total = total + marks
        average = total/n
        print("Average marks of",n,"students is:",average)