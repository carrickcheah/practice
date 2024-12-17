# 125 Valid Palindrome
# python 125.py


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Determines if the input string is a palindrome, ignoring non-alphanumeric characters and case.

        Args:
            s (str): The string to be checked.

        Returns:
            bool: True if 's' is a palindrome, False otherwise.
        """
        # Step 1: Initialize an empty list to store cleaned characters
        cleaned = []

        # Step 2: Iterate over each character in the input string
        for char in s:
            # Check if the character is alphanumeric (letters or numbers)
            if char.isalnum():
                # Convert the character to lowercase and add it to the 'cleaned' list
                cleaned.append(char.lower())

        # Step 3: Create the reversed version of the cleaned list
        reversed_cleaned = cleaned[::-1]  # The [::-1] slice reverses the list


        return cleaned == reversed_cleaned

        # # Step 4: Compare the cleaned list with its reversed version
        # if cleaned == reversed_cleaned:
        #     return True  # The string is a palindrome
        # else:
        #     return False  # The string is not a palindrome

# Example Usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    s1 = "A man, a plan, a canal: Panama"
    print(f"Input: '{s1}'")
    print(f"Is Palindrome? {solution.isPalindrome(s1)}")  # Expected Output: True
    print()


    # Test Case 2
    s2 = "race a car"
    print(f"Input: '{s2}'")
    print(f"Is Palindrome? {solution.isPalindrome(s2)}")  # Expected Output: False
    print()

    # Additional Test Cases
    s3 = ""  # Empty string
    print(f"Input: '{s3}'")
    print(f"Is Palindrome? {solution.isPalindrome(s3)}")  # Expected Output: True
    print()

    s4 = " "  # String with only a space
    print(f"Input: '{s4}'")
    print(f"Is Palindrome? {solution.isPalindrome(s4)}")  # Expected Output: True
    print()

    s5 = "0P"
    print(f"Input: '{s5}'")
    print(f"Is Palindrome? {solution.isPalindrome(s5)}")  # Expected Output: False
    print()
