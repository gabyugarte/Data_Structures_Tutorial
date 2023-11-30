

### Reverse a String using Stack--------------------------------------------------------

def reverse_string(input_string):
    stack = []
    # Push each character onto the stack
    for char in input_string:
        stack.append(char)

    reversed_string = ''
    # Pop each character from the stack to get the reversed string
    while len(stack) > 0:
        reversed_string += stack.pop()

    return reversed_string

# Test the function
input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print("Original String:", input_str)
print("Reversed String:", reversed_str)


