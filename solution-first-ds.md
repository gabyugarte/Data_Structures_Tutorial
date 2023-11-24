
```markdown
```python
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


### Evaluate Balanced Parentheses--------------------------------------------------------


def is_balanced_parentheses(s):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    brackets_map = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or brackets_map[stack.pop()] != char:
                return False

    return len(stack) == 0

# Test cases
print(is_balanced_parentheses("()"))  # Output: True
print(is_balanced_parentheses("()[]{}"))  # Output: True
print(is_balanced_parentheses("(]"))  # Output: False
print(is_balanced_parentheses("([)]"))  # Output: False
print(is_balanced_parentheses("{[]}"))  # Output: True
