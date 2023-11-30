# Linked List (Second Data Structure)

## Introduction to Linked List Data Structure

- **What is a Linked List?**: A linked list is a linear data structure where elements are stored in nodes. Each node contains a data field and a reference (link) to the next node in the sequence.
  
- **Purpose of a Linked List**: Linked lists offer dynamic memory allocation and efficient insertion/deletion operations compared to arrays, as they don't require contiguous memory space.

- **Performance (Big O Notation)**: 
  - Access: O(n)
  - Search: O(n)
  - Insertion/Deletion: O(1) (at the beginning or the end with a reference)

## Implementing a Linked List in Python

- **Types of Linked Lists**: 
  - Singly Linked List
  - Doubly Linked List
  - Circular Linked List

- **Example Python Code**:
  - [Python code for implementing a Singly Linked List](examples/simgly-linked-list.md)
  - [Python code for implementing a Doubly Linked List](examples/doubly-linked-list.md)
  - [Python code for implementing a Circular Linked List](examples/circular-linked-list.md)

## Problems Solved Using Linked List

- **Example Problem: Finding the Middle Element in a Linked List**:
  - This problem involves finding the middle element/node of a linked list. It can be solved using two pointers - one moving twice as fast as the other.
  - [Link to Solution](solutions/second-data-structure/find-midle-element.py)

- **Second Problem (For Student): Reversing a Linked List**:
  - This problem requires reversing the order of nodes in a linked list.
  - [Link to Solution](solutions/second-data-structure/reverse-a-linked-list.py)
