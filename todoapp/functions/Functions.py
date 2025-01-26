FILEPATH="/Volumes/iMacSSD/Arun/Tutorial/Code/Python/udemy/PythonMegaCourse/todoapp/app/todos.txt"
READMODE="r"
APPENDMODE="a"
WRITEMODE = "w"

def get_file_lines(fileName=FILEPATH, mode=READMODE):
    """Function to read lines from the file specified as the function argument"""
    with open(fileName, mode) as file_local:
        lines = file_local.readlines()
        return lines

def write_file_lines(lines, fileName=FILEPATH, mode=WRITEMODE):
    """Function to write lines from the file specified as the function argument"""
    with open(fileName, mode) as file_local:
            file_local.writelines(lines)

def append_file_line(line, fileName=FILEPATH, mode=APPENDMODE):
    """Function to write lines from the file specified as the function argument"""
    with open(fileName, mode) as file_local:
            file_local.writelines(line)