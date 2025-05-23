# What is Stack?

# Stack is a data structure used to store elements in the stack memory. It is working in the LAST IN FIRST OUT (LIFO) order . It has two operations that is (PUSH and POP).
# PUSH - push elements into the stack in one by one order.
# here the first element pushed into the stack will get out as a last element. 
# POP - it will pop the elements from the stack in one by one order.
# here the last element pushed into the stack get out as a first element in the stack.

# Here is an simple example for stack data structure .
# Arr = [1,2,3,4,5,6,7,8]

# 1. PUSH OPERATION

#      |
#     \_/ PUSH

#      8  

#    [   ] <-- top position of the stack memory
#    [ 7 ]
#    [ 6 ]
#    [ 5 ]
#    [ 4 ]
#    [ 3 ]
#    [ 2 ]
#    [_1_] <-- bottom of the stack memory 

# 2. POP OPERATION

#      _
#     / \ POP 
#      |

#      8  - getting out the last element in the as a first element

#    [   ] <-- top position of the stack memory
#    [ 7 ] <- stack pointer
#    [ 6 ]
#    [ 5 ]
#    [ 4 ]
#    [ 3 ]
#    [ 2 ]
#    [_1_] <-- bottom of the stack memory 

# ANOTHER EXAMPLE FOR STACK DATA STRUCTURE
# here your are in home page of a shopping ecommerce website. now you want find a product called "Teddy bear". lets see how stack data structure working here.

# 1. YOU ARE IN THE HOME PAGE

#    [                    ]
#    [                    ]
#    [                    ]
#    [  www.ecom.com/home ] <- here the home page is pushed into the stack memory

# 2. NOW CLICKED THE PRODUCTS PAGE

#    [                         ]
#    [                         ]
#    [  www.ecom.com/products  ] <- here the product page is pushed into the stack memory 
#    [  www.ecom.com/home      ] 

# 3. NOW YOU CLICKED THE SEARCH ICON SO MOVE ON TO SEARCH PAGE

#    [                         ]
#    [  www.ecom.com/search    ] <- here the search page is pushed into the stack memory 
#    [  www.ecom.com/products  ] 
#    [  www.ecom.com/home      ] 

# 4. FINALLY YOU FOUND THAT PRODUCT AND PLACED THE ORDER

#    [  www.ecom.com/productid ] <- here the searched product page is pushed into the stack memory 
#    [  www.ecom.com/search    ] 
#    [  www.ecom.com/products  ] 
#    [  www.ecom.com/home      ] 

# here now you are placed your order successfully and if you want to move on to the home page
# you need get backward in one by one order

# 1. MOVE ON TO SEARCH PAGE

#    [                         ] <- here the productid page is poped out from the stack memory 
#    [  www.ecom.com/search    ] <- moved to next one
#    [  www.ecom.com/products  ] 
#    [  www.ecom.com/home      ] 

# 2. MOVE ON TO PRODUCTS PAGE

#    [                         ] 
#    [                         ] <- here the search page is poped out from the stack memory 
#    [  www.ecom.com/products  ] <- moved to next one
#    [  www.ecom.com/home      ] 

# 3. MOVE ON TO HOME PAGE

#    [                         ] 
#    [                         ]  
#    [                         ] <- here the search page is poped out from the stack memory
#    [  www.ecom.com/home      ] <- moved to next one


# 4. FINALLY IN THE HOME PAGE

#    [                         ] 
#    [                         ]  
#    [                         ] 
#    [  www.ecom.com/home      ] <- NO MORE BACKWARD!

# here the above example is the step by step implementation of stack data structure with example.

# thankyou! 
