# "Given a binary array called nums, return the maximum number of consecutive 1's in the array.
# Input: nums = [1, 1, 0, 1, 1, 1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1, 0, 1, 1, 0, 1]
# Output: 2"


def solution(nums):
    pass


print(solution(([1, 1, 0, 1, 1, 1])))

















# return max number of consecutive 1s

# so loop through list and keep a counter of 1s

# if item in list == 1 and item at the previous index == 1 then counter +=1 

# or I could split up the list at 0s

# create a new counter every time theres a 0

# def solution(nums):
#     listofones = []
#     for i in range(len(nums)):
#         count = 0
#         while i < len(nums) and nums[i] != 0:
#             count += 1
#             i += 1
#         listofones.append(count)
#     return max(listofones)




# def solution2(nums):
#     counter = 0
#     counter_list = []
#     for num in nums:
#         if num == 1:
#             counter += 1
#         else:
#             counter_list.append(counter)
#             counter = 0
#     counter_list.append(counter)
#     return max(counter_list)


# print(solution(([1, 1, 0, 1, 1, 1])))


