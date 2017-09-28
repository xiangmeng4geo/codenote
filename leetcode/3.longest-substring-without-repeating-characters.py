#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters
#
# algorithms
# Medium (24.40%)
# Total Accepted:    354K
# Total Submissions: 1.5M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# Given "bbbbb", the answer is "b", with the length of 1.
# 
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max_len = 1 if len(s) > 0 else 0
        start_cur = 0
        for cur in range(0,len(s)):
           sub_str = s[start_cur:cur]
           cur_str = s[cur]
           find_str = sub_str.find(cur_str)
           if find_str == -1:
               max_len = max(len(sub_str)+1,max_len)
               continue
           else:
               max_len = max(max(find_str+1,len(sub_str)-find_str), max_len)
               start_cur = start_cur + find_str + 1
        return max_len


Solution().lengthOfLongestSubstring('dvdf')
