"""def spy_game(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

result = spy_game([1,2,4,0,0,7,5])
print(result)

result1 = spy_game([1,0,2,4,0,5,7])
print(result1)

result2 = spy_game([1,7,2,0,4,5,0])
print(result2)"""

def spy_game(nums):
    tracker = 0
    for i in nums:
        if i == 0 if tracker<2 else i == 7:
            tracker += 1
            
            
        if tracker == 3:
             return True
         
    return True

print(spy_game([1,2,4,0,0,7,5]))
         
         
         
    
            
            