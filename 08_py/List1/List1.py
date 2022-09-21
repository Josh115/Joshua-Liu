# Since we need to check the last and first elements of the array, take the 0th index and the last index of the array to check if they are equal to 6.
def first_last6(nums):
  return nums[0] == 6 or nums[len(nums) -1] == 6 

first_last6([1, 2, 6]) #→ True
first_last6([1, 2, 3, 8]) #→ False
first_last6([6, 6, 6]) #→ True

#First check to see if the array has at least 1 element, then check to see if the first and last elements are equal.
def same_first_last(nums):
  return len(nums) > 0 and nums[0] == nums[-1]

same_first_last([1, 2, 3]) #→ False
same_first_last([1, 2, 3, 1]) #→ True
same_first_last([]) #→ False

# Return an array with 3, 1, and 4 as its elements.
def make_pi():
  return [3, 1 , 4]

make_pi()

# First check to see if the arrays have the same elements at index 0, then check their last elements.
def common_end(a, b):
  return (a[0] == b[0]) or a[-1] == b[-1]

common_end([1, 2, 3], [7, 3]) #→ True
common_end([1, 2, 3], [7, 3, 2]) #→ False
common_end([1, 2, 3], [1, 3]) #→ True

# Return the sum of all the three elements, nums has len 3.
def sum3(nums):
  return nums[0] + nums[1] + nums[2]

sum3([1, 2, 3]) #→ 6
sum3([5, 11, 2]) #→ 18
sum3([7, 0, 0]) #→ 7

# params: nums- an array of ints has length 3
# return an array with the last 2 elements of nums in the first 2 indicies, then add on the first element of nums in the 3rd index.
def rotate_left3(nums):
  return nums[1:] + nums[:1]

rotate_left3([1, 2, 3]) #→ [2, 3, 1]
rotate_left3([5, 11, 9]) #→ [11, 9, 5]
rotate_left3([0, 0, 1]) #→ [0, 1, 0]

# params: nums- array of ints with length 3
# return nums with a step of -1, which reverses the array.
def reverse3(nums):
  return nums[::-1]

reverse3([1, 2, 3]) #→ [3, 2, 1]
reverse3([5, 11, 9]) #→ [9, 11, 5]
reverse3([2, 1, 2]) #→ [2, 1, 2]


def max_end3(nums):
  if nums[0] > nums[-1]:
    nums[0], nums[1], nums[2] = nums[0], nums[0], nums[0]
  else:
    nums[0], nums[1], nums[2] = nums[2], nums[2], nums[2]

  return nums

def sum2(nums):
  x = 0
  for i in nums[:2]:
    x += i
  return x

def middle_way(a, b):
  return [a[1], b[1]]

def make_ends(nums):
  return [nums[0], nums[-1]]

def has23(nums):
  return 2 in nums or 3 in nums
