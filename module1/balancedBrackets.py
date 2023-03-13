def check_balance(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '[':
            stack.append('[')
        elif bracket == ']':
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False

print(check_balance("]["))
        