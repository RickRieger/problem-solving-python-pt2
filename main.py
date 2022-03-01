# Steps of the software development process:
# 1. Based on a given starting point (feature, task, code block, etc.), what is the 
# expected end result?
# 2. What are the written-out steps to go from point A to point B? You need to 
# solve the problem before you begin coding it.
# 3. Implementation (coding it out, researching)
# 4. Test and debug code (run code with breakpoint, unit test, etc.)
# 5. Refactor if necessary. Test again. This continues until functionality is 
# solidified.
# The above steps should be rinse and repeated for every single problem you 
# encounter. Ignoring these steps or straying from them will result in the long way 
# around to solving a problem or even possibly never solving the problem. 
# To be a good problem solver, it is important to be able to break problems down. 
# One way to go about this is to write out the steps it will take to solve the problem. 
# These steps are written down in English in a manner that are easily explainable to 
# someone who may not be technical. The idea is that in order to code something out,
# you first need to have a good understanding of what it is you are attempting to 
# solve. For each of the problems below, write out the steps it will take to go about 
# solving the problem. Then code it out and test!
# You may jump around in these problems. If you get stuck on one problem, begin 
# working on another. If you get stuck on that new problem, go back to working on 
# the previous one. 
# The use cases below are just examples to give you a better idea of what might be 
# passed into the method or what might be outputted from the method. You shouldn’t
# be coding exactly to these examples, but rather, be flexible to handle any data of 
# that data type.
# Whiteboard Challenges
# 1. Given an array of integers, return indices of the two numbers such that they 
# add up to a specific target. You may assume that each input would 
# have exactly one solution, and you may not use the same element twice.
# a. Use Case:
# i. Given numbers in an array: [5, 17, 77, 50] 
# ii. Target: 55


def find_indices(list, target):
  # check each index of possible pairs to see if they add to target number
  for i in range(0,len(list)):
      for j in range(i,len(list)):
        if list[i] + list[j] == target:
          # expected end result is two numbers
          return [i,j]

print(find_indices([2,3,4,22,4,6], 28))


# 2. Given a number, return the reciprocal of the reverse of the original number, 
# as a double. 
# a. Use case: If given 17, return 0.01408 (1/71)

def recip_reverse(num):
  # make string
  num = str(num)
  # reverse string
  num = num[::-1]
  # reciprocal
  num = 1/int(num)
  # format 5 decimal places to right
  num = "{:.5f}".format(num)
  return num

print(recip_reverse(17))

# 3. A briefcase has a four-digit rolling-lock. Each digit is a number from 0-9 that 
# can be rolled either forwards or backwards. Write a method that returns the 
# smallest number of turns it takes to transform the lock from current 
# combination to the target combination. One turn is equivalent to rolling a 
# number forwards or backwards by one. 
# a. Use case: 
# i. Current lock: 3893
# ii. Target lock: 5296

def to_str(char):
  return str(char)

def how_many_turns(current_lock, target_lock):
  # parse to str for iteration
  current_lock = str(current_lock)
  target_lock = str(target_lock)
  # est count var to keep count of distance
  count = 0
  for i in range(0,len(current_lock)):
    # make sure to continue if same
    if current_lock[i] == target_lock[i]:
      continue
    num1 = int(current_lock[i])
    num2 = int(target_lock[i])
    # little math to compensate for index 0-9
    if num1 < num2:
      count += num2 - num1
    else:
      count += (num2 + 10) - num1 
  # return count
  return count 
print(how_many_turns(3893, 5296)) 


# 4. Given a list of integers, return a bool that represents whether or not all 
# integers in the list can form a sequence of incrementing integers
# a. Use case: 
# i. {5, 7, 3, 8, 6}  false (no 4 to complete the sequence)
# ii. {17, 15, 20, 19, 21, 16, 18}  true

def can_sort_by_increments(list_of_nums):
  list_of_nums.sort()
  for i in range(1,len(list_of_nums)):
    num1 = list_of_nums[i - 1]
    num2 = list_of_nums[i]
    if num2 != num1 + 1:
      return False
  return True

print(can_sort_by_increments([5, 7, 3, 8, 6]))


# 5. Create a method that takes an array of positive and negative numbers. 
# Return an array where the first element is the count of the positive numbers 
# and the second element is the sum of negative numbers. 
# a. Use case: [7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]


def pos_and_neg_num(list_of_nums):
  #instantiate variables to hold values
  pos_count = 0
  neg_sum = 0
  #loop through each number check if its less than or more than 0
  for num in list_of_nums:
    if num < 0:
      neg_sum += num
    elif num > 0:
      pos_count += 1
  return [pos_count, neg_sum]    

print(pos_and_neg_num([7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]))


# 6. Create a method that accepts a string of space separated numbers and 
# returns the highest and lowest number as a string
# a. Use case: “3 9 0 1 4 8 10 2”  “0 10”

def highest_lowest_num(string):
  # make str a list
  list_of_nums = string.split(' ')
  # iterate through list making each value a num for comparison
  for i in range(0, len(list_of_nums)):
    list_of_nums[i] = int(list_of_nums[i])
  print(list_of_nums)
  # use python methods for cal max min values and turn them back to str
  max_num = str(max(list_of_nums))
  min_num = str(min(list_of_nums))
  # return as an f string
  return f'{min_num} {max_num}'

print(highest_lowest_num("3 9 0 1 4 8 10 2"))

# 7. Create a method that accepts a string, check if it’s a valid email address and 
# returns either true or false depending on the valuation. Think about what is 
# necessary to have a valid email address.
# a. Use case:
# i. “mike1@gmail.com”  true
# ii. “gmail.com”  false

def is_valid_email(str):
  # instantiate variables to hold boolean values to check two conditions
  has_dot = False
  has_at_sym = False
  # check each char in str for . or @
  for char in str:
    if char == '.':
      has_dot = True
    elif char == '@':
      has_at_sym = True
  # If both are true, return true, else return false    
  if has_dot and has_at_sym:
    return True
  else:
   return False

print(is_valid_email('gmail.com'))


        
# 8. Create a method that takes in a string and replaces each letter with its 
# appropriate position in the alphabet and returns the string
# a. Use case:
# i. “abc”  “1 2 3”
# ii. “coding is fun”  “3 15 4 9 14 7 9 19 6 21 14”

def alpha_to_pos(string):
  alpha = '1abcdefghijklmnopqrstuvwxyx'
  alpha = list(alpha)
  new_str = ''
  for char in string:
    new_str = new_str + (str(alpha.index(char)) + ' ')
  return new_str

print(alpha_to_pos('hello'))