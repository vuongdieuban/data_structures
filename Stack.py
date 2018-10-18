from pythonds.basic.stack import Stack

""""
@param: parList
parChecker checks if a parentheis () string is balanced
example: (((() -> not balanced
         ((())) -> balanced
Logic: If number of '(' equals to number of ')' then the parathesis string is balanced 
If '(', we store in the stack.
If the next one is ')' then we pop the previous '(' out of the stack
At the end, if stack is empty, that means that there are an equal amount of '(' and ')' in the paraList. Return balanced=True
"""

def parChecker(parList):
    s = Stack()
    balanced = True
    for item in parList:
        if item is '(':
            s.push(item)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
    if s.isEmpty() and balanced is True:
        return balanced
    else:
        balanced = False
        return balanced


symbols = "(()())"
print(parChecker(symbols))