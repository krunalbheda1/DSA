class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        return x_str == x_str[::-1]

solution = Solution()

result = solution.isPalindrome(60016)
print(result)
