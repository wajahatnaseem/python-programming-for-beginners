"""
PYTHON LISTS - CLASSROOM DEMONSTRATION
======================================

Run this file in VS Code and demonstrate each section one by one.

MAIN LIST METHODS:
    append(), clear(), copy(), count(), extend(), index(),
    insert(), pop(), remove(), reverse(), sort()

ALSO COVERED:
    indexing, negative indexing, changing items, len(),
    min(), max(), sum(), in/not in, slicing, +, *,
    for loops, enumerate(), and nested lists.
"""


# ============================================================
# 1. CREATING A LIST
# ============================================================

print("\n" + "=" * 60)
print("1. CREATING A LIST")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango"]

print("Fruits:", fruits)
print("Type:", type(fruits))

# A list can contain different data types.
mixed_list = ["Wajahat", 35, 77.5, True]
print("Mixed list:", mixed_list)


# ============================================================
# 2. ACCESSING ITEMS - INDEXING
# ============================================================

print("\n" + "=" * 60)
print("2. ACCESSING ITEMS - INDEXING")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango", "Orange"]

# Index starts from 0.
print("First item:", fruits[0])
print("Second item:", fruits[1])
print("Third item:", fruits[2])

# Negative indexing starts from the end.
print("Last item:", fruits[-1])
print("Second-last item:", fruits[-2])


# ============================================================
# 3. CHANGING AN ITEM
# ============================================================

print("\n" + "=" * 60)
print("3. CHANGING AN ITEM")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango"]

print("Before:", fruits)

# Lists are mutable, so an existing item can be changed.
fruits[1] = "Orange"

print("After:", fruits)


# ============================================================
# 4. append() - ADD ONE ITEM AT THE END
# ============================================================

print("\n" + "=" * 60)
print("4. append()")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango"]

print("Before:", fruits)

# append() adds ONE item at the end.
fruits.append("Orange")

print("After append:", fruits)


# ============================================================
# 5. insert() - ADD AT A SPECIFIC POSITION
# ============================================================

print("\n" + "=" * 60)
print("5. insert()")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango"]

print("Before:", fruits)

# Syntax:
# list.insert(index, item)

fruits.insert(1, "Orange")

print("After insert(1, 'Orange'):", fruits)

# Existing items are shifted to the right.


# ============================================================
# 6. extend() - ADD MULTIPLE ITEMS
# ============================================================

print("\n" + "=" * 60)
print("6. extend()")
print("=" * 60)

fruits = ["Apple", "Banana"]

print("Before:", fruits)

# extend() adds each item from another list.
fruits.extend(["Mango", "Orange", "Grapes"])

print("After extend():", fruits)

# IMPORTANT DIFFERENCE:

list1 = ["Apple"]
list1.append(["Mango", "Orange"])

print("append() with a list:", list1)
# Result: ['Apple', ['Mango', 'Orange']]

list2 = ["Apple"]
list2.extend(["Mango", "Orange"])

print("extend() with a list:", list2)
# Result: ['Apple', 'Mango', 'Orange']


# ============================================================
# 7. remove() - REMOVE BY VALUE
# ============================================================

print("\n" + "=" * 60)
print("7. remove()")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango", "Banana"]

print("Before:", fruits)

# remove() removes the FIRST occurrence of the value.
fruits.remove("Banana")

print("After remove('Banana'):", fruits)

# If the item may not exist, check first.
if "Orange" in fruits:
    fruits.remove("Orange")
else:
    print("Orange is not in the list.")


# ============================================================
# 8. pop() - REMOVE BY INDEX AND RETURN THE ITEM
# ============================================================

print("\n" + "=" * 60)
print("8. pop()")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Before:", fruits)

# pop() without an argument removes the LAST item.
removed_item = fruits.pop()

print("Removed:", removed_item)
print("After pop():", fruits)

# pop(index) removes an item at a specific index.
removed_item = fruits.pop(1)

print("Removed:", removed_item)
print("After pop(1):", fruits)

# pop() is useful when we need the removed item.


# ============================================================
# 9. clear() - REMOVE EVERYTHING
# ============================================================

print("\n" + "=" * 60)
print("9. clear()")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango"]

print("Before:", fruits)

fruits.clear()

print("After clear():", fruits)


# ============================================================
# 10. index() - FIND POSITION
# ============================================================

print("\n" + "=" * 60)
print("10. index()")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango", "Orange"]

# index() returns the position of the FIRST match.
position = fruits.index("Mango")

print("Mango is at index:", position)

# Optional start position:
numbers = [10, 20, 30, 20, 40]

print("First 20:", numbers.index(20))
print("20 searched from index 2:", numbers.index(20, 2))


# ============================================================
# 11. count() - COUNT OCCURRENCES
# ============================================================

print("\n" + "=" * 60)
print("11. count()")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango", "Banana", "Banana"]

print("Fruits:", fruits)

print("Number of Bananas:", fruits.count("Banana"))
print("Number of Apples:", fruits.count("Apple"))
print("Number of Grapes:", fruits.count("Grapes"))


# ============================================================
# 12. sort() - SORT THE ORIGINAL LIST
# ============================================================

print("\n" + "=" * 60)
print("12. sort()")
print("=" * 60)

numbers = [50, 10, 40, 20, 30]

print("Before:", numbers)

# sort() changes the original list.
numbers.sort()

print("Ascending:", numbers)

# Descending order:
numbers.sort(reverse=True)

print("Descending:", numbers)

# Strings can also be sorted alphabetically.
students = ["Zoya", "Ali", "Sara", "Bilal"]
students.sort()

print("Students sorted:", students)


# ============================================================
# 13. reverse() - REVERSE THE ORIGINAL LIST
# ============================================================

print("\n" + "=" * 60)
print("13. reverse()")
print("=" * 60)

numbers = [10, 20, 30, 40, 50]

print("Before:", numbers)

numbers.reverse()

print("After reverse():", numbers)


# ============================================================
# 14. copy() - CREATE A COPY
# ============================================================

print("\n" + "=" * 60)
print("14. copy()")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango"]

# copy() creates a separate list.
new_fruits = fruits.copy()

print("Original:", fruits)
print("Copy:", new_fruits)

new_fruits.append("Orange")

print("Original after changing copy:", fruits)
print("Copy after change:", new_fruits)


# ============================================================
# 15. len() - NUMBER OF ITEMS
# ============================================================

print("\n" + "=" * 60)
print("15. len()")
print("=" * 60)

students = ["Ali", "Sara", "John", "Ayesha"]

print("Students:", students)
print("Number of students:", len(students))


# ============================================================
# 16. min(), max(), sum()
# ============================================================

print("\n" + "=" * 60)
print("16. min(), max(), sum()")
print("=" * 60)

marks = [85, 72, 91, 64, 88]

print("Marks:", marks)
print("Minimum:", min(marks))
print("Maximum:", max(marks))
print("Total:", sum(marks))

# Average can be calculated using sum() and len().
average = sum(marks) / len(marks)
print("Average:", average)


# ============================================================
# 17. MEMBERSHIP - in / not in
# ============================================================

print("\n" + "=" * 60)
print("17. MEMBERSHIP - in / not in")
print("=" * 60)

students = ["Ali", "Sara", "John", "Ayesha"]

print("Is Sara present?", "Sara" in students)
print("Is Rahul present?", "Rahul" in students)
print("Is Rahul NOT present?", "Rahul" not in students)

if "Sara" in students:
    print("Sara is in the class.")


# ============================================================
# 18. SLICING
# ============================================================

print("\n" + "=" * 60)
print("18. SLICING")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("Original:", fruits)

# Syntax: list[start:end]
# The end index is NOT included.
print("fruits[1:4]:", fruits[1:4])

# Other useful forms:
print("First 3:", fruits[:3])
print("From index 2:", fruits[2:])
print("Last 2:", fruits[-2:])
print("Every second item:", fruits[::2])
print("Reverse using slicing:", fruits[::-1])


# ============================================================
# 19. + OPERATOR - COMBINE LISTS
# ============================================================

print("\n" + "=" * 60)
print("19. + OPERATOR - COMBINE LISTS")
print("=" * 60)

boys = ["Ali", "John"]
girls = ["Sara", "Ayesha"]

all_students = boys + girls

print("Boys:", boys)
print("Girls:", girls)
print("Combined:", all_students)


# ============================================================
# 20. * OPERATOR - REPEAT A LIST
# ============================================================

print("\n" + "=" * 60)
print("20. * OPERATOR - REPEAT A LIST")
print("=" * 60)

numbers = [1, 2, 3]

print("Original:", numbers)
print("Repeated:", numbers * 3)


# ============================================================
# 21. for LOOP WITH A LIST
# ============================================================

print("\n" + "=" * 60)
print("21. for LOOP WITH A LIST")
print("=" * 60)

students = ["Ali", "Sara", "John"]

# The loop processes each item one by one.
for student in students:
    print("Hello", student)


# ============================================================
# 22. for LOOP + if
# ============================================================

print("\n" + "=" * 60)
print("22. for LOOP + if")
print("=" * 60)

marks = [85, 45, 72, 30, 91]

for mark in marks:
    if mark >= 50:
        print(mark, "-> Pass")
    else:
        print(mark, "-> Fail")


# ============================================================
# 23. enumerate() - INDEX + VALUE
# ============================================================

print("\n" + "=" * 60)
print("23. enumerate()")
print("=" * 60)

students = ["Ali", "Sara", "John"]

# enumerate() gives both the index and the value.
for index, student in enumerate(students):
    print(index, student)

# Start counting from 1:
for number, student in enumerate(students, start=1):
    print(number, student)


# ============================================================
# 24. NESTED LISTS
# ============================================================

print("\n" + "=" * 60)
print("24. NESTED LISTS")
print("=" * 60)

# A list can contain other lists.
marks = [
    [80, 75, 90],
    [65, 70, 72],
    [95, 88, 91]
]

print("All marks:", marks)
print("First student's marks:", marks[0])
print("First student's first mark:", marks[0][0])

# Change a nested value:
marks[1][1] = 99

print("After changing:", marks)


# ============================================================
# 25. PRACTICAL - SHOPPING CART
# ============================================================

print("\n" + "=" * 60)
print("25. PRACTICAL - SHOPPING CART")
print("=" * 60)

cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print("Cart:", cart)

if "Mouse" in cart:
    print("Mouse is in the cart.")

cart.remove("Keyboard")

print("After removing Keyboard:", cart)
print("Number of items:", len(cart))


# ============================================================
# 26. PRACTICAL - STUDENT SUBJECTS
# ============================================================

print("\n" + "=" * 60)
print("26. PRACTICAL - STUDENT SUBJECTS")
print("=" * 60)

subjects = ["Python", "Math", "Physics"]

print("Subjects:", subjects)

subjects.append("Cyber Security")
subjects.insert(1, "English")

print("Updated subjects:", subjects)

if "Python" in subjects:
    print("Python is one of the subjects.")

print("Total subjects:", len(subjects))


# ============================================================
# 27. PRACTICAL - FOOD ORDER
# ============================================================

print("\n" + "=" * 60)
print("27. PRACTICAL - FOOD ORDER")
print("=" * 60)

order = []

order.append("Pizza")
order.append("Burger")
order.append("Coke")

print("Current order:", order)

# Customer changes their mind:
order.remove("Coke")

print("After removing Coke:", order)

order.append("Fries")

print("Final order:", order)
print("Number of items:", len(order))


# ============================================================
# 28. ALL 11 LIST METHODS - QUICK REFERENCE
# ============================================================

print("\n" + "=" * 60)
print("28. ALL BUILT-IN LIST METHODS")
print("=" * 60)

print("""
append(x)          -> Add x at the end
clear()             -> Remove all items
copy()              -> Return a shallow copy
count(x)            -> Count occurrences of x
extend(iterable)    -> Add multiple items
index(x)            -> Find first index of x
insert(i, x)        -> Insert x at index i
pop()               -> Remove and return last item
pop(i)              -> Remove and return item at index i
remove(x)           -> Remove first occurrence of x
reverse()           -> Reverse the list in place
sort()              -> Sort the list in place
""")

# Note:
# Python's current built-in list has 11 public methods.
# dir(list) also shows special/dunder methods such as __len__, __add__,
# __getitem__, etc. These are implementation/protocol methods and are
# normally introduced later, not as beginner list methods.


# ============================================================
# 29. METHOD vs FUNCTION
# ============================================================

print("\n" + "=" * 60)
print("29. METHOD vs FUNCTION")
print("=" * 60)

fruits = ["Apple", "Banana", "Mango"]

# METHOD:
# The list object calls the method.
fruits.append("Orange")

# FUNCTION:
# A separate Python function receives the list.
number_of_items = len(fruits)

print("List:", fruits)
print("len() result:", number_of_items)

print("""
METHOD:
    fruits.append("Orange")
    fruits.remove("Apple")
    fruits.sort()

FUNCTION:
    len(fruits)
    min(marks)
    max(marks)
    sum(marks)
""")


# ============================================================
# 30. CLASSROOM SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("30. CLASSROOM SUMMARY")
print("=" * 60)

print("""
A Python list allows us to:

CREATE       -> students = ["Ali", "Sara"]
ACCESS       -> students[0]
CHANGE       -> students[0] = "Ahmed"

ADD:
    append()
    insert()
    extend()

REMOVE:
    remove()
    pop()
    clear()

SEARCH:
    in
    not in
    index()

COUNT:
    count()

ORDER:
    sort()
    reverse()

COPY:
    copy()

MEASURE:
    len()

CALCULATE:
    min()
    max()
    sum()

EXTRACT:
    slicing -> students[0:2]

COMBINE:
    list1 + list2

REPEAT:
    list * 3

PROCESS:
    for loop

Remember:
    list_name.method()
""")

print("\n" + "=" * 60)
print("END OF PYTHON LISTS DEMONSTRATION")
print("=" * 60)
