# CONCATENATION
list1 = [2,4,6,8]
list2 = [1,3,5,7,9]
list = list1 + list2
print(list)
# can only concatenate list to list not list to str....

#REPITATION
list1 = ["hello"]
list = list1*4
print(list)

#MEMBERSHIP - CHECK ELEMENT PRSENT IN LIST GIVE TRUE
list5 = ['BLACK', 'RED']
print('RED' in list5)

#SLICING - SLICING operations allows to create new list by taking out  elements from an existing lists.
list1 = ['black','red','green','blue','yellow','violet']
print(list1[2:4])
print(list1[::2])

#Traversing a list
list1 = ['blue','black','red','yellow','green']
for item in list1:
    print(item)

for i in range(len(list1)):
    print(list1[i])

