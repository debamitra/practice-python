# "r", "w", "a" , "r+"
# *args *kwargs
# internally args is a tuple
# kwargs - extra keywords arguments in a dict 
with open("notes.txt", "w") as f:
    f.write("Hello World\n")
    f.write("This is a new line")

with open("notes.txt") as f:
    content = f.read()
    print(content)



with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())


# Write a function that:
#	1.	Takes a filename and a list of strings
#	2.	Writes each string on a new line
#	3.	Then reads and returns the content as a list

def process_file(filename, mylist):
    with open(filename,"w") as f:
        for item in mylist:
            f.write(item + "\n")
    with open(filename,"r") as f:
        newlist = []
        for item in f:
            newlist.append(item.strip())
    return newlist

print(process_file("notes.txt", ["hello","myname","islucy"]))