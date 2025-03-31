# y = [x for x in range(10_000_000)]
# z = (x for x in range(10_000_000))



import dis # disassembler of python bytecode

def make_list():
    return [x for x in range(10)]

def make_gen():
    return (x for x in range(10))

print("List comprehension")
dis.dis(make_list)
print("\nGenerator Expression")
dis.dis(make_gen)