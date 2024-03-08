def isPalindrome(s):
    rev = ''.join(reversed(s))
    
    if s == rev:
        return True
    return False
        
        
s = input()
answer = isPalindrome(s)

if (answer):
    print("Yes")
else:
    print("No")

