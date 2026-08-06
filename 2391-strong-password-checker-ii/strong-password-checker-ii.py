class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        if len(password) < 8:
            return False
            
        u = 0  
        l = 0 
        d = 0 
        s = 0  
        
        for i in range(len(password)):
            char = password[i]
        
            if i < len(password) - 1 and char == password[i + 1]:
                return False
                
            if char.isupper():
                u += 1
            elif char.islower():
                l += 1
            elif char.isdigit():
                d += 1
            elif not char.isalnum() and not char.isspace():
                s += 1
           
        return u > 0 and l > 0 and d > 0 and s > 0