from todoapp.functions import Functions
import PySimpleGUI as sg
import _tkinter
import time

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=10 , key="Add")
list_box = sg.Listbox(values=Functions.get_file_lines(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event,values =  window.read()
    print(event)
    print("------------------------------")
    print(f"Values={values}")
    match event:
        case "Add":
            try:
                new_todo = values["todo"]
                todos_local = Functions.get_file_lines()
                todos_local.append(new_todo+"\n")
                Functions.write_file_lines(todos_local)
                window["todos"].update(todos_local)
            except:
                print(f"Error")

        case "Edit":
            try:
                to_edit = values["todos"][0]
                todos_local = Functions.get_file_lines()
                index = todos_local.index(to_edit)
                new_todo = values["todo"]
                todos_local[index] = (new_todo+"\n")
                Functions.write_file_lines(todos_local)
                window["todos"].update(todos_local)
                window["todo"].update("")
            except:
                print(f"Error")
        case "Complete":
            try:
                to_remove= values["todos"][0]
                todos_local = Functions.get_file_lines()
                index = todos_local.index(to_remove)
                removed_todo = todos_local.pop(index)
                print(to_remove)
                print(removed_todo)
                Functions.write_file_lines(todos_local)
                window["todos"].update(todos_local)
                window["todo"].update("")
            except:
                print(f"Error")
        case "Exit":
            exit()
exit()
window.read()
print("Hello")

