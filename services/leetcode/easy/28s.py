class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Step 1: Identify the Problem
        - We need to find the first occurrence of a substring (`needle`) in a string (`haystack`).
        - If the `needle` is not found, return `-1`.

        Step 2: Understand the Solution
        - Use string searching techniques to locate the starting index of the first occurrence.
        - If `needle` is an empty string, return `0` (by convention).

        Step 3: Define Parameters and Requirements
        - Input:
            * `haystack` (string): The main string where we search.
            * `needle` (string): The substring to find.
        - Constraints:
            * 1 <= len(haystack), len(needle) <= 10^4
            * Both strings contain only lowercase English characters.

        Step 4: Plan Step-by-Step Execution
        1. Handle edge case: If `needle` is an empty string, return `0`.
        2. Check if `needle` is a substring of `haystack` using a loop or Python's built-in string methods.
        3. If found, return the index of the first occurrence.
        4. If not found, return `-1`.

        Step 5: Implement and Validate
        - Use Python's `find()` method, which returns the index of the first occurrence or `-1` if not found.
        - Test with examples to ensure correctness.
        
        Full Solution for Beginners:
        - Handle special cases, like an empty `needle`.
        - Use a simple and intuitive approach like `find()`.
        - Include examples and explanations for clarity.
        """
        # Handle edge case: empty needle
        if not needle:
            return 0

        # Use the built-in `find` method to locate the first occurrence
        index = haystack.find(needle)

        # Return the index (or -1 if not found)
        return index

# Example Usage for Beginners:
solution = Solution()

# Example 1
haystack1 = "sadbutsad"
needle1 = "sad"
print(solution.strStr(haystack1, needle1))  # Output: 0

# Example 2
haystack2 = "leetcode"
needle2 = "leeto"
print(solution.strStr(haystack2, needle2))  # Output: -1

# Example 3: Edge case
haystack3 = "hello"
needle3 = ""
print(solution.strStr(haystack3, needle3))  # Output: 0

# DOS-Style Flowchart Representation:
# +-----------------------------+
# | Start                       |
# +-----------------------------+
#             |
#             v
# +-----------------------------+
# | Is `needle` empty?          |
# +-----------------------------+
#       | Yes           | No
#       v               v
# +-------------+   +----------------------------+
# | Return 0    |   | Use `find()` to locate     |
# +-------------+   | the first occurrence of    |
#                   | `needle` in `haystack`     |
#                   +----------------------------+
#                            |
#                            v
# +------------------------------------------------+
# | Found?                                         |
# +------------------------------------------------+
#       | Yes (index >= 0)         | No (index == -1)
#       v                          v
# +-------------------------+   +-----------------+
# | Return index of match   |   | Return -1       |
# +-------------------------+   +-----------------+
