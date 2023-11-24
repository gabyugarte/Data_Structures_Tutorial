## STACK (First Data Structure)

### Introduction to Stack Data Structure

- **What is a Stack?**  
  A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle. Elements are added and removed from the stack at the same end, known as the top. It operates with two main operations: push (adds an element to the top) and pop (removes the top element).

- **Purpose of a Stack**  
  Stacks are used to manage function calls in programming (call stack), undo mechanisms in software, and in algorithms like depth-first search (DFS). They provide a simple and efficient structure for storing and managing data.

- **Performance (Big O Notation)**  
  - Push Operation: O(1)
  - Pop Operation: O(1)
  - Peek Operation (Viewing the top element without removal): O(1)

### Implementing a Stack in Python

- **Operations: Push, Pop, Peek**  
  In Python, a stack can be implemented using lists. The `append()` method is used for push, `pop()` method for pop, and accessing the last element using indexing for peeking.

- **Example Python Code**  
  ```python
  class Stack:
      def __init__(self):
          self.items = []

      def push(self, item):
          self.items.append(item)

      def pop(self):
          if not self.is_empty():
              return self.items.pop()
          else:
              return None

      def peek(self):
          if not self.is_empty():
              return self.items[-1]
          else:
              return None

      def is_empty(self):
          return len(self.items) == 0

  # Example Usage
  stack = Stack()
  stack.push(1)
  stack.push(2)
  print(stack.peek())  # Output: 2
  stack.pop()
  print(stack.peek())  # Output: 1
  
### Problems Solved Using Stack

- **First Problem: Reverse a String using Stack**  
  Implement a function to reverse a string using a stack data structure.

- **Second Problem (For Student): Evaluate Balanced Parentheses**  
  Implement a function to check whether a given string of parentheses is balanced using a stack.
  - [Link to Solution](solution-first-ds.md)
