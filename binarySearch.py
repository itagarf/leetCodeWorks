#Given an array of integers nums which is sorted in ascending order, and an integer target, 
#write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#You must write an algorithm with O(log n) runtime complexity.



def b_search(nums, target):
  beg_index = 0
  end_index = len(nums)-1

  while beg_index <= end_index:
    midpoint = (beg_index + end_index) // 2     #double slash gives you integer division instead of normal division
    mid_value = nums[midpoint]

    if mid_value == target:
      return midpoint

    elif mid_value < target:
      beg_index = midpoint + 1

    else:
      end_index = midpoint - 1

  return -1

num1 = [1,3,5,6,7,9,14,17,22]
#if not sorted, use "num1.sort()"
#num1 = [14,22,17,1,3,5,9,6,7]
#num1.sort()
target1 = 9

b_search(num1, target1)