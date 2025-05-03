# Hash functions will convert the key into a hash value
# Hash value is an index (integer) of the value you are going to store 
# Hash value is used to find the index for the key in the hashmap

# for example 
# Apple --> H() --> hash value --> (8) index 
# It uses ASCII for the letters in the key

# APPLE -> KEY
# A - 65
# p - 112
# p - 112
# l - 108
# e - 101
# SUM = 65+112+112+108+101 = 498

# these are the ASCII numbers for the alphabatical letters

# MOD(498,10) -> 8 (index to store the value)
#         10 is the size of the array

# COMPLEXITY

# 1. Look up by key is O(1) on average
# 2. Insertion and Deletion is O(1) on average

# COLLISION

# The collision is called index repeataion. when we pass a key into the Hash function it gives the same index sometimes
# For example
# HM['Banana'] -> Index value is 7
# HM['Strawberry'] -> Index value is 7

# So it replaces the previous value with the new one. Data lost has occured.

# This are the solutions to get rid of the collisions.
1. Separate chaining 
2. Linear probing

# 1. Separate Chaining

# whenever the index found for the two values then it will use linked list data structure 
# on that index to store multiple values one by one.

# Example :

# (index) - values by seperate chaining
# 0 - 24
# 1
# 2
# 3 - 35 -> 45 -> 22
# 4
# 5 - 33

# 2. Linear Probing

# Whenever collision occurs on a particular index then it will store the current value in  
# the available index by using the linear search method to find an empty place in the 
# array. (Implment linear search from the current index to find an empty index)

# Example :

# 0 - ("A",34)
# 1 - ("B",44)
# 2 - ("D",22) Inserted value to index 2 instead of index 5
# 3
# 4 
# 5 - ("C",43) Store the next value ("D",22) on the index 2 because no space after index 5 so it will store the (key,value) ("D",22) by using linear search algorithm.
