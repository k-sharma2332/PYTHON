# List -> sequence of itmes separated by commas and enclosed in sequare bracket[5,33.4,"New delhi","2a"] It contain different types of data. it can be changed.
list1 = [2,4,6,8,10]
print(list1)
list2 = ["a","e","i","o","u"]
print(list2)

#ACCESSING ELEMENTS IN THE LIST
print(list1[0])
print(list1[2+2])
print(list1[-1]) #return first element form right
# list of the list1 is assigned to n
n = len(list1)
print(n)
# get the last element of list1
print(list1[n-1])
# get the first element of list1
print(list1[-n])

#List are mutable
list3 = ['blue','black','orange','yellow']
print(list3)
list3[2] = 'red'
print(list3)