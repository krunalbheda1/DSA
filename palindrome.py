class Solution(object):
    def isPalindrome(self, x):
          return str(x) == str(x)[::-1]

solution = Solution()

result = solution.isPalindrome(6006)
print(result)
