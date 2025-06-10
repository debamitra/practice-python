from textutils.cleaner import remove_whitespace
from textutils.formatter import capitalize_words


def write_to_file(filename,lines):
    with open(filename,'w') as f:
        for line in lines:
            f.write(line + '\n')

def read_and_process_file(filename):
    processed_lines = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                cleaned = remove_whitespace(line)
                formatted = capitalize_words(cleaned)
                processed_lines.append(formatted)
    except FileNotFoundError:
        print("File not found")
    return processed_lines




lines = ["   hello world", "good   MORNING", " this is  a test "]
filename = "input.txt"

write_to_file(filename,lines)

final_output = read_and_process_file(filename)
print("Processed lines:")
for i in final_output:
    print("-",i)





