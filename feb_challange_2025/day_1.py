# 3151. Special Array I

num =[2,1,4]
# num =[4,3,1,6]

class Solution(object):
    def isArraySpecial(self, num):
        for i in range(len(num)-1):
            if(num[i]%2 == num[i+1]%2):
                return(False)
        return(True)

output = Solution()
print(output.isArraySpecial(num))
