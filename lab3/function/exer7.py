def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False 

result1 = has_33([1,3,3])
print(result1)

result2 = has_33([1,3,1])
print(result2)

result3 = has_33([3,1,3])
print(result3)