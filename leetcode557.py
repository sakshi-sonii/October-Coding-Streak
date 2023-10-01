class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda word: word[::-1], s.split()))
    
solution = Solution()
input_string = "Let's take LeetCode contest"
result = solution.reverseWords(input_string)
print(result)