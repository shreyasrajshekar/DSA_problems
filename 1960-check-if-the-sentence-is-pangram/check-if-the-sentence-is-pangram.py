class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        flag=0
        allalp="abcdefghijklmnopqrstuvwxyz"
        for char in allalp:
            if char not in sentence:
                flag=1
                break
        if flag==1:
            return False
        return True