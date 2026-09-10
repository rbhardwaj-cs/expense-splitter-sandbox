def average(numbers_list):
    if len(numbers_list) == 0:
        return 0 
    
    
    return sum(numbers_list) / len(numbers_list)

def find_max(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)

    return False


