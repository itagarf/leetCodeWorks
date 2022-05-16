#I pick a number from 1 to n. You have to guess which number I picked.
#Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        begining = 0
        ending = n
        
        while begining <= ending:
            midpoint = (begining + ending) // 2
            apiValue = guess(midpoint)
            
            if apiValue == 0:
                return midpoint
            elif apiValue == 1:
                begining = midpoint + 1
            elif apiValue == -1:
                ending = midpoint - 1