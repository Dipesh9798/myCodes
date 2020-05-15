class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:  # Remove all.
            return '0'

        stack = []
        removed = 0
        for c in num:
            while stack and stack[-1] > c and removed < k:
                stack.pop()
                removed += 1

            stack.append(c)

        while stack and removed < k:
            stack.pop()
            removed += 1

        rslt = ''.join(stack).lstrip('0')
        if not rslt:
            return '0'

        return rslt

###############################################################
##                     ANOTHER METHOD                        ##
###############################################################

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k:
            return "0"
        for i in range(k):
            for j in range(len(num)-1):
                if num[j] > num[j+1]:
                    num = num[:j]+num[j+1:]
                    break
            else:
                num = num[:-1]
        return str(int(num))
        
