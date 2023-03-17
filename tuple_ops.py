#TUPLE operations
a_tuple = (11,22,33,44,69)
print(type(a_tuple))

#Access elements
print(a_tuple[0])
print(a_tuple[1])
print(a_tuple[2])
print(a_tuple[3])
print(a_tuple[4])

#Count
print(a_tuple.count(22))

#Index, return index of a given element
print(a_tuple.index(69))

#3 ways to append to a tuple
#List conversion
a = list(a_tuple)
a.append('Hello')
new_tuple = tuple(a)
print(new_tuple)

#Tuple concatenation
a_tuple = a_tuple + ('Hello Again',)
print(a_tuple)

#Tuple unpacking
a_tuple = (*a_tuple,888888)
print(a_tuple)
