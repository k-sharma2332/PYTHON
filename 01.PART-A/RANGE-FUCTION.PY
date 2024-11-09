# RANGE() FUCTION - range([start], stop[, step])
# It is used to create a list containing a sequence of integers from the given start value upto stop value with a difference of the given step value. If start value is not specified, by default the list starts from 0. If step is also not specified, by default the value is increment by 1 in each iteration.All parameters of range() fuction must be integers. The step parameter can be a positive or a negative integer excluding zero.

print(list(range(10)))
print(list(range(2,10)))
print(list(range(0,30,5)))
print(list(range(0,-9,-1)))
print(list(range(2,-8,-2)))

# print the program for multiple of 5
for num in range(5):
    if num>0:
        print(num*5)