def read_file(filename):
    try:
        with open(filename,"r") as f:
            text = f.read()
            print(text)
    except FileNotFoundError as e:
        print("File doesnt exist")
        print(e)

read_file("notes1.txt")