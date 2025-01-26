from todoapp.functions import Functions

options = """
    Enter 1 or Add to Enter a Todo
    Enter 2 or Edit to Edit the Todo
    Enter 3 or Complete to remove the Todo
    Enter 4 or Show to show the Todo List
    Enter 5 or Exit to Exit
"""

while True:
    choice = input(options).strip(" ")

    match choice:
        case "1" | "Add":
            todo_item = input(f"Enter the Todo Item:")
            Functions.append_file_line(todo_item + "\n")
        case "2" | "Edit":
            index = int(input("Enter the index of the item to Edit"))
            todos = Functions.get_file_lines()
            if index>len(todos) | index<1:
                print(f"Invalid index : {index}")
            else:
                index_local = index -1
                new_todo = input("Enter the updated todo Item: ")
                todos[index_local] = new_todo + "\n"
                Functions.write_file_lines(todos)
        case "3" | "Complete":
            index = int(input("Enter the index of the item to Remove"))
            todos = Functions.get_file_lines()
            if index>len(todos)| index<1:
                print(f"Invalid index : {index}")
            else:
                index_local = index -1
                to_remove_todo = todos[index_local]
                removed_todo = todos.pop(index_local)
                print(f"Item to remove:{to_remove_todo}... Removed Item:{removed_todo}")
                Functions.write_file_lines(todos)
        case "4" | "Show":
            todos = Functions.get_file_lines()
            for index, todo in enumerate(todos):
                todo_local = todo.strip("\n")
                print(f"{index+1} : {todo_local}")
        case "5" | "Exit":
            break;
print(f"Exiting application.BYEEEE!!!!")