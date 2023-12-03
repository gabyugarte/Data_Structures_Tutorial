

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
'''The provided test case demonstrates how the reverse_string function successfully reverses the input string "Hello, World!" using a stack, resulting in the output "!dlroW ,olleH".'''

input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print("Original String:", input_str)
print("Reversed String:", reversed_str)

'''Algorithm Explanation:
Using a Stack:

The algorithm initializes an empty stack to hold characters.
It iterates through each character in the input string and pushes each character onto the stack.
Reversing the String:

After pushing all characters onto the stack, the algorithm initializes an empty string reversed_string.
It pops each character from the stack one by one and appends them to reversed_string.'''

'''Step-by-Step Execution:
Initializing the Stack:

The input string "Hello, World!" is iterated character by character.
Each character is pushed onto the stack.
Reversing the String:

After the stack contains all characters from the input string, the algorithm starts popping characters from the stack.
These characters are concatenated in reverse order, constructing the reversed string.'''