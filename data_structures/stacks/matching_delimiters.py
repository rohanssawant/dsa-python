"""
This shows application of a stack by testing pairs of matching delimiters. In our first application, we consider arithmetic expressions that may contain various pairs of grouping symbols, such as
• Parentheses:`(` and `)`  
• Braces:`{` and `}`  
• Brackets:`[` and `]`

Each opening symbol must match its corresponding closing symbol. For example, a left bracket,“[,” must match a corresponding right bracket, “],” as in the expression 
[(5+x)-(y+z)].

• Correct:   ()(()){([()])} 
• Correct:   ((()(()){([()])})) 
• Incorrect: )(()){([()])} 
• Incorrect: ({[])} 
• Incorrect: (
"""

from arr_based_implementation import ArrayStack

def checkDelimiters(expression: str) -> bool:
    left = '({['
    right = ')}]'
    myStack = ArrayStack()
    
    for char in expression:
        if char in left:
            myStack.push(char)
        elif char in right:
            if myStack.is_empty():
                return False  # Nothing to pair with
            popped_char = myStack.pop(char)
            if right.index(popped_char) != left.index(popped_char):
                return False
    return myStack.is_empty()            