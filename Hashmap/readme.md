# Hash functions will convert the key into a hash value
# Hash value is an integer
# Hash value is used to find the index of the key in the hashmap

# for example 
# Apple --> H() --> hash value --> (8) index 
# It uses ASCII for the letters in the key

# A - 65
# p - 112
# p - 112
# l - 108
# e - 101
# SUM = 65+112+112+108+101 = 498

# these are the ASCII numbers for the alphabatical letters

# MOD(498,10) -> 8
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

