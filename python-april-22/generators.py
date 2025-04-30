def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count = count + 1

for num in count_up_to(3):
    print(num)


gen = (x*x for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))


#Reading big files line by line
def read_large_file(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()