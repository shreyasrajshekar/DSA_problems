class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        l=list(s)
        for i in range(len(l)):
            p=l.pop(0)
            l.append(p)
            s1="".join(l)
            if s1==goal:
                return True
        return False