brackets_string = input("Enter a sequence of brakets: ")

open = ["("]
close = [")"]

def Check(myStr):
    stack = []
    for i in myStr:
        if i in open:
            stack.append(i)
        elif i in close:
            pos = close.index(i)
            if ((len(stack) > 0) and
                (open[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return -1
    if len(stack) == 0:
        return 1
    else:
        return -1
    
Res = Check(brackets_string)
if Res == 1:
    print("Balanced brackets sequence")
else:
    print("Unbalanced brackets sequence")