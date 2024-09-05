def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode="w", encoding="utf-8") as test_file:
        test_file.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode="a", encoding="utf-8") as test_file:
        test_file.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt", mode="r", encoding="utf-8") as test_file:
        for line in test_file:
            return line

#Function Calls
write_file("test_file", "This is a test content.")
append_file("test_file", "\nAppended content.")
read_file("test_file")