def open_file(file_path="default.txt", mode="r"):
    try:
        file = open(file_path, mode)
        return file
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
file = open_file("w")
if file:
    file.write("Hello, World!")
    file.close()
