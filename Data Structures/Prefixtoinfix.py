def prefixtoinfix(prefix):
    stack = []
    i = len(prefix) - 1    # read prefix expression in reverse order
    while i >= 0:
        if not isOperator(prefix[i]):    #  if symbol is operand push it to stack
            stack.append(prefix[i])
        else:
            """if symbol is operator pop two operands from the stack and create a string
            by concatenating the two operands and the operator between them and push the resultant string 
            back to stack """
            str = f"({stack.pop()}{prefix[i]}{stack.pop()})"
            stack.append(str)
        i -= 1
    return stack.pop()
def isOperator(p):
    return p in ["+", "-", "*", "/", "^", "(", ")"]
string=input("Enter string")
print("Infix expression is :",prefixtoinfix(string))
"""
Output: Enter string:"*+ab/ef"
Infix expression is : ((a+b)*(e/f)) 
"""