# Step-by-Step Guide for Solving "Roman to Integer"

# Step 1: Understand the Problem
# Roman numerals represent numbers using specific symbols (I, V, X, etc.).
# To convert a Roman numeral to an integer:
# - Add the value of each symbol.
# - Subtract when a smaller value comes before a larger value (e.g., IV = 4).
# The task is to compute the integer equivalent of a valid Roman numeral string.

# Step 2: Define What Needs to Happen
# 1. Create a mapping of Roman symbols to their integer values.
# 2. Traverse the string from left to right.
# 3. For each symbol:
#    - If the current value is smaller than the next value, subtract it.
#    - Otherwise, add it.
# 4. Accumulate the total integer value.

# Step 3: Plan How to Rearrange the Array
# - Use a dictionary for symbol-to-value mapping.
# - Loop through the string "s".
# - Compare the current symbol's value to the next symbol's value:
#   - If current < next: subtract.
#   - Otherwise: add.

# Step 4: Determine the Result
# - At the end of the loop, the accumulated sum will be the integer value of the Roman numeral.

# Step 5: Test Your Solution
# Test with examples:
# Input: "III"   Output: 3   (I + I + I = 3)
# Input: "LVIII" Output: 58  (L + V + III = 58)
# Input: "MCMXCIV" Output: 1994 (M + CM + XC + IV = 1994)

# Step 6: Think About Edge Cases
# - Single-character input: "I" = 1, "M" = 1000.
# - Input with only subtraction cases: "IV", "IX", "XL", etc.
# - Large inputs near the upper limit: "MMMCMXCIX" = 3999.

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral string to an integer.

        Args:
            s (str): The Roman numeral string.

        Returns:
            int: The integer equivalent of the Roman numeral.
        """
        # Step 1: Create a mapping of Roman symbols to their integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Step 2: Initialize total and previous value
        total = 0
        prev_value = 0

        # Step 3: Loop through the Roman numeral string in reverse
        for char in reversed(s):
            # Get the integer value of the current Roman symbol
            current_value = roman_to_int[char]

            # Step 4: Determine if we need to add or subtract
            if current_value < prev_value:
                total -= current_value  # Subtract if a smaller value precedes a larger value
            else:
                total += current_value  # Otherwise, add the value

            # Update the previous value
            prev_value = current_value

        # Step 5: Return the total integer value
        return total

# Example usage:
solution = Solution()
print(solution.romanToInt("III"))    # Output: 3
print(solution.romanToInt("LVIII"))  # Output: 58
print(solution.romanToInt("MCMXCIV")) # Output: 1994
