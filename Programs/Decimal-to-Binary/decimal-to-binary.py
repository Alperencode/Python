def decimalToBinary(n):
    # Successive division
    stack = []
    while n>0:
        # push the remainder on top of the stack
        stack.insert(0, n%2)
        # divide the number by 2
        n = n//2

    # return stack as a string
    return "".join(str(i) for i in stack)

print(decimalToBinary(155))