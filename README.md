# linked-list

## Project Overview

---
This project implements two variants of list data structures containing characters (type `Character`):
1. **Array-based list** — a list implemented using Python’s built-in list.
2. **Singly linked circular list** — a linked list where the last node points back to the first node.

The project includes unit tests covering all functionality and is integrated with CI (GitHub Actions) to automatically run tests on every push.

## Variant Information

---
- Group list number: 26  
- Variant = 26 mod 4 = 2  

This means:
- Initial implementation: Array-based list  
- Refactored implementation: Singly linked circular list

## Running the project

---

Run the demo script to see all list methods in action:

```
python main.py
```

Run the unit tests:

```
python -m unittest test_list.py
```

## Failed Cl commit

---
https://github.com/Ederatone/linked-list/commit/4b5c77aa292ad758a8b42dc26fc8920490db3c9a

## Conclusions

---

This lab changed my perspective on software development:

- Unit tests helped catch bugs early and gave me confidence during refactoring
- CI ensured that broken code was quickly detected
- Writing tests initially felt time-consuming, but saved a lot of time during debugging
- Now I see tests and CI as essential tools, not optional extras