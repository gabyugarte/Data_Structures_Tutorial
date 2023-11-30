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

