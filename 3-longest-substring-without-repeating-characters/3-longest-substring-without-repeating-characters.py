class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_len = start = 0
        for i, char in enumerate(s):
            # 사용했던 문자라면
            if char in used and start <= used[char]:
                start = used[char] + 1
            # 처음 나오는 문자라면
            else:
                max_len = max(max_len, i - start + 1)
            used[char] = i
            print(max_len)
        return max_len