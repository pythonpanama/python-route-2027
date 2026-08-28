"""Exercise 3: conditionals.

Complete the conditions. The program should say whether a person can take the
workshop based on an age of 18 or more, and whether they requested support.
"""

age = int(input("Age: "))
requested_support = input("Requested an accessibility support? (yes/no): ").strip().lower()

if age >= 18:
    print("Eligible for the adult workshop.")
else:
    print("This workshop is for adults. Please do not collect extra information.")

if requested_support == "yes":
    print("Record the request through the private event process.")
else:
    print("No support request was entered.")
