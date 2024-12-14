"""
14. Longest Common Prefix
 
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:


                # +----------------------------+
                # | Start                     |
                # +----------------------------+
                #             |
                #             v
                # +----------------------------+
                # | Is the input list empty?    |
                # | (strs == [])                |
                # +----------------------------+
                #     | Yes                     | No
                #     v                         v
                # +------------------+       +--------------------------+
                # | Return ""        |       | Set prefix = strs[0]     |
                # +------------------+       +--------------------------+
                #                                 |
                #                                 v
                #                 +--------------------------------+
                #                 | For each string in strs[1:]   |
                #                 +--------------------------------+
                #                                 |
                #                                 v
                #                 +---------------------------------------+
                #                 | Does string start with prefix?       |
                #                 +---------------------------------------+
                #                     | Yes              | No
                #                     v                  v
                #                 +----------------+  +--------------------------+
                #                 | Keep prefix    |  | Shorten prefix by 1 char |
                #                 +----------------+  | (prefix = prefix[:-1])   |
                #                                     +--------------------------+
                #                                             |
                #                                             v
                #                 +----------------------------------------+
                #                 | Is prefix empty after shortening?      |
                #                 +----------------------------------------+
                #                         | Yes               | No
                #                         v                   v
                #                     +---------------+    +----------------+
                #                     | Return ""     |    | Continue loop  |
                #                     +---------------+    +----------------+
                #                                             |
                #                                             v
                #                             +-------------------------------+
                #                             | Return the final prefix value |
                #                             +-------------------------------+


