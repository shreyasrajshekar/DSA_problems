class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]

        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                l.append(s[i:j])
        c=0
        for k in range (len(l)):
            if l[k]==l[k][::-1]:
                c+=1
        return c
