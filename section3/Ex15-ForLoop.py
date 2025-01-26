question="""In the coding area, we have created a members list. Below that line, write a for-loop block that:
(1) iterates over the items of the members list, and
(2) prints out each item of the list with the first letter capitalized.

In other words, here is what your program should print out:

John
Sarah
Dora
----------------------------------------------------------
"""

print(f"QUESTION={question}")
members = ["john", "sarah", "dora"]

for item in members:
    print(item.capitalize())

for ind, item in enumerate(members):
    print(f'{ind} : {item}')
