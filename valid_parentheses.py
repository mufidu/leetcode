# Make a function to detect valid parentheses
# and return True if the parentheses are valid
# and False if they are not valid
# Example valid: ()()()(), ({[]}), (()), (), []()

def is_valid(s):
    # create a dictionary to store the parentheses
    # and their corresponding closing parentheses
    parentheses = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    # create a stack to store the parentheses
    stack = []
    # loop through the string
    for char in s:
        # if the char is an opening parentheses
        if char in parentheses.values():
            # push the char to the stack
            stack.append(char)
        # if the char is a closing parentheses
        elif char in parentheses.keys():
            # if the stack is empty
            if not stack:
                # return False
                return False
            # if the stack is not empty
            else:
                # if the top of the stack is not the
                # corresponding closing parentheses
                if stack[-1] != parentheses[char]:
                    # return False
                    return False
                # if the top of the stack is the
                # corresponding closing parentheses
                else:
                    # pop the top of the stack
                    stack.pop()
    # if the stack is not empty
    if stack:
        # return False
        return False
    # if the stack is empty
    else:
        # return True
        return True


print(is_valid('({[]}))'))
