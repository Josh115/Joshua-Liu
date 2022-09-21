# params: nums - an array of ints.
# use a for loop to check every element of the array for even-ness. increment count by 1 if it is, then return count at the end.
def count_evens(nums):
  count = 0
  for i in nums:
    if i % 2 == 0:
      count += 1
  return count

count_evens([]) #→ 0
count_evens([2]) #→ 1
count_evens([2, 1, 2, 2, 40]) #→ 4

# params: nums - array of length 1 or more.
# max(nums) returns the largest element in nums, min(nums) returns the smallest.
# return their difference.
def big_diff(nums):
  return max(nums) - min(nums)

big_diff([2, 3]) #→ 1
big_diff([2]) #→ 0
big_diff([100, -100]) #→ 200

# params: nums is an array of len 3 or more.
# add up all the elements of the array with a for loop, the subtract the largest and smallest values from the sum.
# finally divide by the total number of elements minus 2 because of the min and max values being excluded.
def centered_average(nums):
  x, y, z = max(nums), min(nums), 0
  for i in nums:
    z += i
  z = z - y
  z = z - x
  return int(z/(len(nums)-2))

centered_average([1, 2, 3, 4, 100]) #→ 3
centered_average([1, 1, 5, 5, 10, 8, 7]) #→ 5
centered_average([-10, -4, -2, -4, -2, 0]) #→ -3

# params: nums is an an array of ints
# use a loop to iterate through nums, checking to see if the current element is equal to 13, if it is, then skip over it and the element after it.
# if not, then add the element to the sum.
def sum13(nums):
  sum, i = 0, 0
  while i < len(nums):
    if nums[i] == 13:
      i+=2
    else:
      sum+=nums[i]
      i+=1
  return ct

sum13([13, 1, 2, 13, 2, 1, 13]) #→ 3
sum13([]) #→ 0
sum13([1, 2, 2, 1, 13]) #→ 6

#params: nums is an array of ints
#
def sum67(nums):
  inBetween = False
  sum = 0
  for i in nums:
    if i == 6:
      inBetween = True
    if not inBetween:
      sum+=i
    if i == 7:
      inBetween = False
  return sum

def has22(nums):
  for i in range(len(nums) -1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False
