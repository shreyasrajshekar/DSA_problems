class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        l = list(map(int, str(num)))
        for i in range(len(l)):
            if l[i]!=9:
                l[i]=9
                break
            else:
                continue
        return int(''.join(map(str, l)))
        