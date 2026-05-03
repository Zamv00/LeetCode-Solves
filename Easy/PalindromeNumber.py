def isPalindrome(x):
    strx = str(x)
    if (strx[::-1] == strx):
        return True
    
    return False
    