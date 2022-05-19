#Let's call an array arr a mountain if the following properties hold:
#arr.length >= 3
#There exists some i with 0 < i < arr.length - 1 such that:
#arr[0] < arr[1] < ... arr[i-1] < arr[i]
#arr[i] > arr[i+1] > ... > arr[arr.length - 1]
#
#Given an integer array arr that is guaranteed to be a mountain, 
#return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


def peakIndexInMountainArray(arr):
  i = 0
  peakIndex = 0
  while i < (len(arr) - 1):
    #if the element in current index position is less than the next element, then it isnt at the peak index, 
    #so increment the index position and check that and the next element.
    if arr[i] < arr[i+1]:
      peakIndex = i+1
    else:          #if it isnt less than the next element, it is the peak index
      return peakIndex
    i +=1    #keep incrementing till i = len(arr)-1


arr1= [0,1,0]
arr2 = [0,3,10,5,2]
arr3 = [0,2,4,5,14,7,3,1]
peakIndexInMountainArray(arr3)