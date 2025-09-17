def isValid(s):
    my_stack = []
    dict_s = {")":"(", "}":"{", "]":"["}
    for i in s:
        if i not in dict_s: # opening bracket
            my_stack.append(i)
            print(my_stack)
        else: # closing bracket
            print(my_stack[-1], dict_s[i])
            if my_stack and my_stack[-1] == dict_s[i]:
                my_stack.pop()
            else:
                return False # mismatch or empty stack
    return not my_stack
    

s = "{}"
print(isValid(s))