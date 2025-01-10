def find_duplicates(arr):
    # python automatically calls iter(arr) and returns iterator object over 
    # which it then repeatedly calls next(iterator) until StopIteration is raised
    myset = set()
    for i in arr:
        if i in myset:
            return True
        else:
            myset.add(i)
    return False

print(find_duplicates([3,4,5,6,1,2,4]))