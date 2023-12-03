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

'''The provided test cases demonstrate how the function determines whether the input strings contain balanced parentheses or not, returning True for balanced cases and False otherwise.'''
# Test cases
print(is_balanced_parentheses("()"))  # Output: True
print(is_balanced_parentheses("()[]{}"))  # Output: True
print(is_balanced_parentheses("(]"))  # Output: False
print(is_balanced_parentheses("([)]"))  # Output: False
print(is_balanced_parentheses("{[]}"))  # Output: True

'''Algorithm Explanation:
Stack Utilization:

A stack is used to keep track of opening parentheses encountered in the string.
Bracket Mapping:

Sets opening_brackets and closing_brackets are defined to identify opening and closing brackets, respectively.
The brackets_map dictionary contains pairs of opening and closing brackets as key-value pairs.
Iterating through the String:

The code iterates through each character in the input string s.
For each character:
If it's an opening parenthesis (i.e., '(', '[', '{'), it's added to the stack.
If it's a closing parenthesis (')', ']', '}'):
If the stack is empty or the top of the stack doesn't correspond to the expected opening parenthesis for the current closing parenthesis, the function returns False.
If they match, the last opened parenthesis is removed from the stack.
Final Validation:

After iterating through the entire string:
If the stack is empty, it means all opening parentheses found their respective closing parentheses, and the function returns True.
If the stack is not empty, some opening parentheses don't have corresponding closing parentheses, and the function returns False.'''