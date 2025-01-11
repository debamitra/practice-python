# https://leetcode.com/studyplan/top-interview-150/


# Binary Search

# 35. Search Insert Position
# EASY
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end ) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

searchInsert([1,3,5,6], 5)

##############################################

# 74. Search a 2D Matrix
# MEDIUM
def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m * n - 1
        while start <= end:
            mid = (start + end) / 2
            print(mid)
            i = mid / n
            j = mid % n
            print(matrix[i][j])
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

        
searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)


##########################################################

# 162. Find Peak Element
# MEDIUM

# Non Binary search solution - O(N), optimize for O(log N)
def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 1:
            return 0
        if size == 2:
            return nums.index(max(nums[0],nums[1]))
        for i in range(size):
            if i == 0 and nums[i+1] < nums[i]:
                return i
            if i == size - 1  and nums[i-1] < nums[i]:
                return i
            if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                return i
        return -1