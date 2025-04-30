# "r", "w", "a" , "r+"

with open("notes.txt", "w") as f:
    f.write("Hello World\n")
    f.write("This is a new line")

with open("notes.txt") as f:
    content = f.read()
    print(content)