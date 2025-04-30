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




# Write a generator function `countdown(n)` that yields n, n-1, ..., 0

# Example:
# for i in countdown(3):
#     print(i)
# Output: 3 2 1 0


def countdown(n):
    while n >= 0:
        yield n
        n = n-1

for i in countdown(3):
    print(i)




# Create a generator `evens_up_to(n)` that yields even numbers up to `n` (inclusive)

# Example:
# list(evens_up_to(10)) → [0, 2, 4, 6, 8, 10]


def evens_up_to(n):
    num =0
    while num <= n:
        if num % 2 == 0:
            yield num
        num = num+1
print(list(evens_up_to(10)))
