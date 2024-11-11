# Write a program to allow user to perform any those list operation given in a menu. The menu is:
myList = [22,4,16,38,13]
choice = 0
for attempt in range (3): print("Attempt number:",attempt)
print("The list 'myList' has the following element",myList)
print("\nL I S T O P E R A T I O N S")
print(" 1. Append an element")
print(" 2. Insert an element at the desired position")
print(" 3. Append a list to the given list")
print(" 4. Modify an existing element")
print(" 5. Delete an existing element by its position")
print(" 6. Delete an existing element by its value")
print(" 7. Sort the list in ascending order")
print(" 8. Sort the list in decending order")
print(" 9. Display the list")
choice = int(input("ENTER YOUR CHOICE(1-9): "))

#append element
if choice == 1:
    element = eval(input("Enter the element to be appended: "))
    myList.append(element)
    print("The element has been appended\n")

#insert an element at desired position
elif choice == 2:
      element = eval(input("Enter the element to be inserted: "))
      pos = int(input("Enter the position: "))
      myList.insert(pos,element)
      print("The element has been inserted\n")

#append a list to the given list
elif choice == 3:
       newList = eval(input("Enter the list to be appended: "))
       myList.extended(newList)
       print("The list has been appended\n")

#modify an existing element
elif choice == 4:
      i = int(input("Enter the position of the element to be modified: "))
      if i < len(myList):
            newElement = eval(input("Enter the new element: "))
            oldElement = myList[i]
            myList[i] = newElement
            print("The element",oldElement,"has been modified\n")
      else:
            print("Position of the element is more then the length of list")

#delete an existing element by position
elif choice == 5:
      i = int(input("Enter the position of the element to be deleted: "))
      if i < len(myList):
            element = myList.pop(i)
            print("The element",element,"has been deleted\n")
      else:
            print("\nPosition of the element is more  then the length of list")

#delete an existing element by value
elif choice == 6:
      element = int(input("\nEnter the element to be deleted: "))
      if element in myList:
            myList.remove(element)
            print("\nThe element",element,"has been deleted\n")
      else:
            print("\nElement",element,"is not present in the list")

#list in sorted order
elif  choice == 7:
      myList.sort()
      print("\nThe list has been sorted")

#list in reversed order
elif choice == 8:
      myList.sort(reverse = True)
      print("\nThe list has been sorted in reverse order")

#display the list
elif choice == 9:
      print("\nThe list is:", myList)
else:
      print("Choice is not valid")

