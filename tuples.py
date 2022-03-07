mytupel = ('Max') # type := string
print(type(mytupel))
mytupel = ('Max',) # tuple := tuple
print(type(mytupel))
mytupel = ('Max', 28, "Dhk") # tuple := tuple
print(type(mytupel))
mytupel = 'Max', 28, "Dhk"
print(type(mytupel))

print(mytupel[0]) # Access tuple item
print(mytupel[-1]) # Access tuple item

if "Max" in mytupel:
    print("yes")
else:
    print("no")

mytuple = ('a', 'p', 'p', 'l', 'e')
print(mytuple.count('p')) # Number of item in the tuple
print(mytuple.index('l')) # First index of item in the tuple

my_list = ['Max', 28, "Dhk"]
mytupel = (my_list) # list => tuple convert
my_list = list(mytupel) # tuple => list convert

# [ start : end : step ]
print(mytupel[1:3]) # slicing tuple

my_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple
print(i1) # first item := 0
print(i3) # last item := 4
print(i2) # rest of the item := (1, 2, 3)


import sys
my_list = [0,1,2,3, "hello", True]
my_tuple = (0,1,2,3, "hello", True)
print(sys.getsizeof(my_list), "bytes") # Larger than tuple size
print(sys.getsizeof(my_tuple), "bytes") # Smaller than tuple size

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000)) # Takes more time than Tuple to make list
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000)) # takes less time than list to making a tuple