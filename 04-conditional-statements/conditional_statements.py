# Python IF Statements — Classroom Demonstration
# Run this file in VS Code and demonstrate each section one by one.

print("=" * 70)
print("PYTHON IF STATEMENTS — CLASSROOM DEMONSTRATION")
print("=" * 70)


# 1. SIMPLE IF
print("\n1. SIMPLE IF")
print("-" * 70)

age = 20

# The indented code runs only when the condition is True.
if age >= 18:
    print("You are an adult.")

print("Program continues...")


# 2. IF WITH COMPARISON OPERATORS
print("\n2. IF WITH COMPARISON OPERATORS")
print("-" * 70)

marks = 85

# >   greater than
# <   less than
# >=  greater than or equal to
# <=  less than or equal to
# ==  equal to
# !=  not equal to



if marks >= 75:
    print("You scored 75 or more.")


# 3. IF...ELSE
print("\n3. IF...ELSE")
print("-" * 70)

age = 16

# True -> if block
# False -> else block
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")


# 4. IF...ELIF...ELSE
print("\n4. IF...ELIF...ELSE")
print("-" * 70)

marks = 82

# Python checks conditions from top to bottom.
# The first True condition is executed.
if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: F")


# 5. MULTIPLE INDEPENDENT IF STATEMENTS
print("\n5. MULTIPLE INDEPENDENT IF STATEMENTS")
print("-" * 70)

marks = 95

# These are separate if statements.
# Python checks ALL three conditions.
if marks >= 40:
    print("Pass")

if marks >= 75:
    print("Good performance")

if marks >= 90:
    print("Excellent performance")

# Compare with elif:
print("\nSame value using elif:")

if marks >= 90:
    print("Excellent performance")
elif marks >= 75:
    print("Good performance")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")


# 6. NESTED IF
print("\n6. NESTED IF")
print("-" * 70)

age = 20
has_id = True

# An if statement inside another if statement is a nested if.
if age >= 18:
    print("Age requirement satisfied.")

    if has_id:
        print("Entry allowed.")
    else:
        print("Please show your ID.")
else:
    print("Entry not allowed because you are under 18.")


# 7. IF WITH AND
print("\n7. IF WITH AND")
print("-" * 70)

age = 20
has_ticket = True

# AND means ALL conditions must be True.
if age >= 18 and has_ticket:
    print("You can enter the event.")
else:
    print("You cannot enter the event.")


# 8. IF WITH OR
print("\n8. IF WITH OR")
print("-" * 70)

day = "Saturday"

# OR means at least ONE condition must be True.
if day == "Saturday" or day == "Sunday":
    print("It is the weekend.")
else:
    print("It is a weekday.")


# 9. IF WITH NOT
print("\n9. IF WITH NOT")
print("-" * 70)

logged_in = False

# NOT reverses True and False.
if not logged_in:
    print("Please log in first.")


# 10. IF WITH IN / NOT IN
print("\n10. IF WITH IN / NOT IN")
print("-" * 70)

fruit = "apple"

# 'in' checks whether a value exists in a collection.
if fruit in ["apple", "banana", "mango"]:
    print("We have this fruit.")

# 'not in' checks that the value does not exist.
if fruit not in ["orange", "grapes"]:
    print("Fruit is not orange or grapes.")


# 11. IF WITH STRINGS
print("\n11. IF WITH STRINGS")
print("-" * 70)

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful.")
else:
    print("Invalid username or password.")


# 12. IF WITH NUMBERS — EVEN OR ODD
print("\n12. IF WITH NUMBERS — EVEN OR ODD")
print("-" * 70)

number = 17

# % gives the remainder.
# Even numbers have remainder 0 when divided by 2.
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")


# 13. IF WITH BOOLEAN VARIABLES
print("\n13. IF WITH BOOLEAN VARIABLES")
print("-" * 70)

is_raining = True

# A Boolean variable already contains True or False.
# Therefore, it can be used directly as the condition.
if is_raining:
    print("Take an umbrella.")
else:
    print("No umbrella needed.")

# Prefer:
# if is_raining:
# over:
# if is_raining == True:


# 14. IF WITH MULTIPLE CONDITIONS
print("\n14. IF WITH MULTIPLE CONDITIONS")
print("-" * 70)

age = 22
is_student = True
has_id = True

if age >= 18 and is_student and has_id:
    print("Student entry approved.")
else:
    print("Entry requirements not satisfied.")


# 15. ELIF WITH AND / OR
print("\n15. ELIF WITH AND / OR")
print("-" * 70)

marks = 78
attendance = 85

if marks >= 75 and attendance >= 75:
    print("Grade A — good marks and attendance.")
elif marks >= 75:
    print("Good marks, but check attendance.")
elif attendance >= 75:
    print("Good attendance, but marks need improvement.")
else:
    print("Both marks and attendance need improvement.")


# 16. CHECKING A RANGE
print("\n16. CHECKING A RANGE")
print("-" * 70)

age = 25

# Python allows chained comparisons:
# 18 <= age <= 60
#
# This means:
# age is greater than or equal to 18
# AND age is less than or equal to 60
if 18 <= age <= 60:
    print("Age is between 18 and 60.")


# 17. CHECKING WHETHER A VALUE EXISTS
print("\n17. CHECKING WHETHER A VALUE EXISTS")
print("-" * 70)

students = ["Ali", "Sara", "John", "Priya"]
name = "Sara"

if name in students:
    print(name, "is present in the list.")
else:
    print(name, "is not present in the list.")


# 18. IF WITH TRUTHINESS
print("\n18. IF WITH TRUTHINESS")
print("-" * 70)

name = "Wajahat"

# A non-empty string is considered True.
if name:
    print("Name has been provided.")

name = ""

# An empty string is considered False.
if not name:
    print("Name is empty.")

students = ["Ali", "Sara"]

# A non-empty list is considered True.
if students:
    print("The list contains students.")

students = []

# An empty list is considered False.
if not students:
    print("The list is empty.")


# 19. CONDITIONAL EXPRESSION — ONE-LINE IF/ELSE
print("\n19. CONDITIONAL EXPRESSION — ONE-LINE IF/ELSE")
print("-" * 70)

age = 20

# Useful when choosing between two values.
message = "Adult" if age >= 18 else "Minor"

print(message)


# 20. PRACTICAL EXAMPLE — ATM
print("\n20. PRACTICAL EXAMPLE — ATM")
print("-" * 70)

balance = 5000
withdraw_amount = 3000
pin_correct = True

if pin_correct:
    print("PIN accepted.")

    if withdraw_amount <= balance:
        balance = balance - withdraw_amount
        print("Please collect your cash.")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance.")
else:
    print("Incorrect PIN.")


# QUICK REFERENCE
print("\n" + "=" * 70)
print("QUICK REFERENCE")
print("=" * 70)

print("""
1. Simple if:
       if condition:
           action

2. if...else:
       if condition:
           action
       else:
           other_action

3. if...elif...else:
       if condition1:
           action1
       elif condition2:
           action2
       else:
           action3

4. Multiple independent if:
       if condition1:
           action1
       if condition2:
           action2

5. Nested if:
       if condition1:
           if condition2:
               action

6. AND:
       if condition1 and condition2:

7. OR:
       if condition1 or condition2:

8. NOT:
       if not condition:

9. Membership:
       if value in collection:
       if value not in collection:

10. Conditional expression:
       result = value1 if condition else value2
""")

print("=" * 70)
print("END OF DEMONSTRATION")
print("=" * 70)
