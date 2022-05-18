#Given a sorted array of distinct integers and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.

def searchInsert(nums, target):
  if not target in nums:
      nums.append(target)
      nums.sort()
  begining = 0
  ending = len(nums)-1

  while begining <= ending:
    mid = (begining + ending) // 2
    mp = nums[mid]

    if mp < target:
      begining = mid + 1
    elif mp > target:
      ending = mid - 1
    elif mp == target:
      return mid
  return mid


nums1 = [2,3,5,7,9,10]
target1 = 6
searchInsert(nums1, target1)