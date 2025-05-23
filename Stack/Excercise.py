# Exercise for stack

# 1.Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
#   reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

# Implementation 

# reverse string using stack datastructure

from Stack import Stack

def reverseString(Str):
    # initialized the stack module
    stack = Stack()
    # take char one by one from the Str variable and push it into the stack using push() method [TC : (O(n))]
    for each in Str:
        stack.push(each)
    
    # created a variable and concatenate each stack element into it by using the pop() method [TC : (O(n))]
    reversedString = []
    for _ in range(len(Str)):
        reversedString.append(stack.pop())
    print("".join(reversedString))


reverseString("We will conquere COVID-19")

# 2. Write a function in python that checks if paranthesis in the string are balanced or not.
#    Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial. 

# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

def isBalanced(Str):
    stack = Stack()
    # Matching of closing to opening brackets
    matching = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for char in Str:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                return False
            if stack.pop() != matching[char]:
                return False
    return stack.is_empty()

print(isBalanced("({a+b})")) 
print(isBalanced("))((a+b}{")) 
print(isBalanced("((a+b))")) 
print(isBalanced("))")) 
print(isBalanced("[a+b]*(x+2y)*{gg+kk}")) 