class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        tasks.sort()
        d={}
        count=0
        for i in tasks:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        

        for v in d.values():
            if v == 1:
                return -1
            count += (v + 2) // 3

        return count