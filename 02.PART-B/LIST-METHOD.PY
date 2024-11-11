#len() - Return the length of the list passed as the argumet.
list1 = [10,20,30,40,50]
print(len(list1))

#lisst() - Creates an empty list of an argument is passed.
list2 = list()
print(list2)

# Create a list if a sequence is passed as an argument.
str1 = 'aeiou'
list1 = list(str1)
print(list1)

#append() - Append a single element passed as an argument at the end of the list. A list can also be appended as an element to an existing list.
list1 = [10,20,30]
list1.append(50)
print(list1)

list1 = [10,20,30,40]
list1.append([50,60])
print(list1)

#extend() - Append each element of the list passed as argument at the end of the given list
list1 = [10,20,30,40]
list2 = [50,60]
list1.extend(list2)
print(list1)

#insert() - Insert an element at a particular index in the list.
list1 = [10,20,30,40,50]
#insert element 25 at index value 2 
list1.insert(2,25)
print(list1)

#count() - Return the number of times a given element appears in the list.
list1 = [10,20,30,40,50,30,10,30,20,20,20]
print(list1.count(20))

#find() - Return index of the first occurence of the element in the list. If the element is not present, ValueError is generated.
list1 = [10,20,30,40,50,10,20,40,50]
print(list1.index(20))

#remove() - Remove the given element from the list.If the element is present multiple times, only the first occurenece is removed.If the element is not present, then ValueError is generated.
list1 = [10,20,30,40,50,30]
list1.remove(30)
print(list1)

#pop() - Returns the element whose index is passed as argument to the function and also remove it from the list.If no arument is given, then it returns and removes the last element of the list.
list1 = [10,20,30,40,50]
list1.pop(3)
print(list1)

#reverse() - Reverse the order of element in the given list.
list1 = [223,45,442,455,24,65,34,34,324,54]
list1.reverse()
print(list1)
list2 = ['khushi','sharma','kirti','bhardwaj']
list2.reverse()
print(list2)

#sort() - Sorts the element of the given list in place.
list1 = ['khushi','shraddha','nisha','shourya']
list1.sort()
print(list1)

#sorted() - It takes a list as parameter and creates a new list consisting of the same element but arranged in ascending order.
list1 = [24,3345,425,4323,24,454]
list2 = sorted(list1)
print(list1)
print(list2)

#min() - Return minimum or smallest element of the list.
list1 = [23,45,11,67,85,56]
print(min(list1))
print(max(list1))
print(sum(list1))