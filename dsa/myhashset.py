class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for i in range(self.size) ]

    def _hash(self,key):
        return key % self.size
    
    

    

hs = MyHashSet()
print(hs.__dict__)

# def two_sum(nums, target):
#     count = 0
#     if len(nums) < 2:
#         return 0
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)-1):
#             if(nums[i]+nums[j] == target):
#                 count = count + 1
#     return count

# print(two_sum([1,2,3,4,5], 5))