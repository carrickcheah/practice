from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Step 1: Identify the Problem
        - We need to find the longest common prefix shared by all strings in the array.
        - If there is no common prefix, return an empty string "".

        Step 2: Understand the Solution
        - A common prefix is a set of letters that all strings start with, like a shared beginning.
        - If the array has "flower", "flow", and "flight", the prefix "fl" is common.
        - For "dog", "racecar", and "car", there is no common prefix, so we return "".

        Step 3: Define Parameters and Requirements
        - Input: An array of strings (e.g., ["flower", "flow", "flight"]).
        - Constraints:
            * 1 <= strs.length <= 200
            * 0 <= strs[i].length <= 200
            * strs[i] consists of only lowercase English letters.

        Step 4: Plan Step-by-Step Execution
        1. If the list is empty, return "".
        2. Start with the first string as a "base prefix".
        3. Compare the base prefix with the next string.
        4. Reduce the base prefix until it matches the start of the current string.
        5. Repeat for all strings.

        Step 5: Implement and Validate
        - Write code to follow the steps above.
        - Test with examples to make sure the function works.
        
        Full Solution for Beginners:
        - Start by handling edge cases such as an empty list.
        - Use the first string as a reference and compare it to the others.
        - Gradually shorten the prefix to find the common starting sequence.
        """
        if not strs:
            # If the list is empty, return an empty string
            return ""

        # Use the first string as the initial prefix
        prefix = strs[0]

        # Iterate through the rest of the strings in the list
        for string in strs[1:]:
            while not string.startswith(prefix):
                # Shorten the prefix by removing the last character
                prefix = prefix[:-1]

                # If the prefix becomes empty, return an empty string
                if not prefix:
                    return ""

        # Return the longest common prefix after checking all strings
        return prefix

# Example Usage for Beginners:
# Create an instance of the Solution class
solution = Solution()

# Example 1
strings1 = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strings1))  # Output: "fl"

# Example 2
strings2 = ["dog", "racecar", "car"]
print(solution.longestCommonPrefix(strings2))  # Output: ""
