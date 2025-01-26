question = """Write a script that:

(1) prints out the methods of the list type, and

(2) prints out the help of the list.count method.
----------------------------------------------------
"""

print(f"QUESTION={question}")
listMethod = dir(list)
print(listMethod)
print(help(list.count))
print(listMethod)