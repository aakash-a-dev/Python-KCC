mytuple = (1, 2, 3, 4, 5)
 
# tuples are indexed
print(mytuple[1])
print(mytuple[4])
 
# tuples contain duplicate elements
mytuple = (1, 2, 3, 4, 2, 3)
print(mytuple)

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'kcc')
 
# Concatenating above two
print(tuple1 + tuple2)

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'kcc')
 
tuple3 = (tuple1, tuple2)
print(tuple3)

tuple3 = ('python',)*3
print(tuple3)


# code to test slicing
tuple1 = (0 ,1, 2, 3)
 
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])