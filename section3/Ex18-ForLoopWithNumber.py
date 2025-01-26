question = """Write a program that:

(1) iterates over the scores list, and
(2) prints out each item.
Here is what the output of the program would look like:

11
34
98
43
45
54
54
---------------------------------
"""

print(f"QUESTION={question}")
scores = [11, 34, 98, 43, 45, 54, 54]
print("-------------Listing Numbers---------------")

for num in scores:
    print(num)

scores.sort()
print("-------------Listing Sorted Numbers---------------")

for num in scores:
    print(num)